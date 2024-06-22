import pathlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import cv2

mpl.rcParams.update(
    {
        "font.size": 10,
    }
)

# Load labels for the Kinetics-600 dataset
labels_path = tf.keras.utils.get_file(
    fname="labels.txt",
    origin="https://raw.githubusercontent.com/tensorflow/models/f8af2291cced43fc9f1d9b41ddbf772ae7b0d7d2/official/projects/movinet/files/kinetics_600_labels.txt",
)
labels_path = pathlib.Path(labels_path)
lines = labels_path.read_text().splitlines()
KINETICS_600_LABELS = np.array([line.strip() for line in lines])
KINETICS_600_LABELS[:20]


# Function to load video from file
def load_video_from_file(file_path, image_size=(224, 224)):
    """Loads a video from a file into a TF tensor.

    Use images resized to match what's expected by your model.
    The model pages say the "A2" models expect 224 x 224 images at 5 fps

    Args:
        file_path: Path to the video file.
        image_size: a tuple of target size.

    Returns:
        a video loaded from the file
    """
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


# Load video from file
video_file_path = (
    "/Users/hetanthakkar/Downloads/teeth.mp4"  # Replace with your video file path
)
video = load_video_from_file(video_file_path)
print(video.shape)

# Load the MoViNet model
id = "a2"
mode = "base"
version = "3"
hub_url = f"https://tfhub.dev/tensorflow/movinet/{id}/{mode}/kinetics-600/classification/{version}"
model = hub.load(hub_url)
sig = model.signatures["serving_default"]

# Make predictions
logits = sig(image=video[tf.newaxis, ...])
logits = logits["classifier_head"][0]


# Function to get top_k labels and probabilities
def get_top_k(probs, k=5, label_map=KINETICS_600_LABELS):
    # Sort predictions to find top_k
    top_predictions = tf.argsort(probs, axis=-1, direction="DESCENDING")[:k]

    # Collect the labels of top_k predictions
    top_labels = tf.gather(label_map, top_predictions, axis=-1)

    # Decode labels
    top_labels = [label.decode("utf8") for label in top_labels.numpy()]

    # Top_k probabilities of the predictions
    top_probs = tf.gather(probs, top_predictions, axis=-1).numpy()

    return tuple(zip(top_labels, top_probs))


# Get probabilities and print top_k labels and probabilities
probs = tf.nn.softmax(logits, axis=-1)
for label, p in get_top_k(probs):
    print(f"{label:20s}: {p:.3f}")
