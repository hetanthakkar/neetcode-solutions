import time
import heapq


class Twitter:

    def __init__(self):
        self.follow_map = {}
        self.user_tweet_map = {}
        self.tweet_time_map = {}

    def postTweet(self, userId, tweetId):
        if userId not in self.user_tweet_map:
            self.user_tweet_map.update({userId: [tweetId]})
        else:
            self.user_tweet_map[userId].append(tweetId)
        self.tweet_time_map.update({tweetId: time.time()})

    def getNewsFeed(self, userId):
        ans = []
        connections = []
        if userId in self.follow_map:
            connections = self.follow_map[userId]
        connections.append(userId)
        tweet_ids = []
        for user in connections:
            if user in self.user_tweet_map:
                for i in self.user_tweet_map[user]:
                    tweet_ids.append(i)
        tweet_time_map = {}
        for tweet in tweet_ids:
            tweet_time_map.update({tweet: self.tweet_time_map[tweet]})
        heap = [(-value, key) for key, value in tweet_time_map.items()]
        largest = heapq.nsmallest(10, heap)
        largest = [(key, -value) for value, key in largest]
        for i in largest:
            ans.append(i[0])
        return ans

    def follow(self, followerId, followeeId):
        if followerId in self.follow_map:
            self.follow_map[followerId].append(followeeId)
        else:
            self.follow_map[followerId] = [followeeId]

    def unfollow(self, followerId, followeeId):
        if followerId in self.follow_map:
            self.follow_map[followerId].remove(followeeId)


twitter = Twitter()
# twitter.postTweet(1, 5)
twitter.follow(1, 2)
twitter.follow(2, 1)
# twitter.getNewsFeed(2)
# twitter.postTweet(2, 6)
# twitter.getNewsFeed(1)
# twitter.getNewsFeed(2)
# twitter.unfollow(1, 2)
