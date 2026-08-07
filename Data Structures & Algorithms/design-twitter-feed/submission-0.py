import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list)    # userId -> list of [timestamp, tweetId]
        self.followmap = defaultdict(set)    # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Add self-follow to see own tweets
        self.followmap[userId].add(userId)

        for followeeId in self.followmap[userId]:
            if self.tweetmap[followeeId]:
                index = len(self.tweetmap[followeeId]) - 1
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId] and followeeId != followerId:
            self.followmap[followerId].discard(followeeId)
