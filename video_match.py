import pathlib
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import cv2
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import imageio

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")


labels_path = tf.keras.utils.get_file(
    fname="labels.txt",
    origin="https://raw.githubusercontent.com/tensorflow/models/f8af2291cced43fc9f1d9b41ddbf772ae7b0d7d2/official/projects/movinet/files/kinetics_600_labels.txt",
)
labels_path = pathlib.Path(labels_path)
lines = labels_path.read_text().splitlines()
KINETICS_600_LABELS = np.array([line.strip() for line in lines])

id = "a2"
mode = "base"
version = "3"
hub_url = f"https://tfhub.dev/tensorflow/movinet/{id}/{mode}/kinetics-600/classification/{version}"
model = hub.load(hub_url)
sig = model.signatures["serving_default"]

frame_buffer = []
buffer_size = 1


def preprocess_frame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = tf.image.resize(frame, (224, 224))
    frame = tf.cast(frame, tf.float32) / 255.0
    return frame


def get_top_k(probs, k=5, label_map=KINETICS_600_LABELS):
    top_predictions = tf.argsort(probs, axis=-1, direction="DESCENDING")[:k]
    top_labels = tf.gather(label_map, top_predictions, axis=-1)
    top_labels = [label.decode("utf8") for label in top_labels.numpy()]
    top_probs = tf.gather(probs, top_predictions, axis=-1).numpy()
    return tuple(zip(top_labels, top_probs))


@socketio.on("connect")
def handle_connect():
    print("Client connected")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")


# Function to load video from file
def load_video_from_file(file_path, image_size=(224, 224)):
    cap = cv2.VideoCapture(file_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = tf.image.resize(frame, image_size)
        frame = tf.cast(frame, tf.float32) / 255.0
        frames.append(frame)
    cap.release()
    video = tf.stack(frames, axis=0)
    return video


@socketio.on("video_frame")
def handle_video_frame(data):
    frame_bytes = data["frame"]
    nparr = np.frombuffer(frame_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if frame is not None:
        frame = preprocess_frame(frame)
        frame_buffer.append(frame)

        if len(frame_buffer) >= buffer_size:
            video_clip = np.array(frame_buffer)
            frame_buffer.clear()  # Clear the buffer for the next clip

            # Convert frames to uint8
            video_clip = (video_clip * 255).astype(np.uint8)

            # Save the frames as a GIF
            gif_path = "/tmp/video_clip.gif"
            imageio.mimsave(gif_path, video_clip, fps=4)

            # Load the GIF for prediction
            video = load_video_from_file(gif_path)
            logits = sig(image=video[tf.newaxis, ...])
            logits = logits["classifier_head"][0]
            probs = tf.nn.softmax(logits, axis=-1)
            top_k_results = get_top_k(probs)
            results = [
                {"label": label, "probability": float(prob)}
                for label, prob in top_k_results
            ]
            print(results, "results")
            emit("prediction", results)
    else:
        print("Frame decoding failed")


if __name__ == "__main__":
    socketio.run(app)
