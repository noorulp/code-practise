import heapq

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = {}
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        hashSet = self.tweets.get(userId, None)
        self.count += 1
        item = ((self.count, tweetId))
        if hashSet is None:
            self.tweets[userId] = set()
        self.tweets[userId].add((item))
        if self.followers.get(userId, None) == None:
            self.followers[userId] = set()
            self.followers[userId].add(userId)

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        maxSize = 10
        for id in self.followers.get(userId, []):
            for tweet in self.tweets.get(id, []):
                if len(heap) < maxSize:
                    heapq.heappush(heap, (tweet[0], tweet[1]))
                elif heap[0][0] < tweet[0]:
                    heapq.heappushpop(heap, (tweet[0], tweet[1]))
        feed = []
        while heap:
            feed.append(heapq.heappop(heap)[1])        
        return feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if self.followers.get(followerId, None) == None:
            self.followers[followerId] = set()
            self.followers[followerId].add(followerId)
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.followers.get(followerId, None) and followeeId in self.followers[followerId]:
            self.followers.get(followerId).remove(followeeId)


def test(funcs: list, vals: list):
    twitter = Twitter()
    i = 1
    while i < len(funcs):
        f = funcs[i]
        v = vals[i]
        if f == "postTweet":
            twitter.postTweet(v[0], v[1])
        elif f == "getNewsFeed":
            print(twitter.getNewsFeed(v[0]))
        elif f == "follow":
            twitter.follow(v[0], v[1])
        elif f == "postTweet":
            twitter.postTweet(v[0], v[1])
        elif f == "unfollow":
            twitter.unfollow(v[0], v[1])
        i += 1

if __name__ == '__main__':
    funcs = ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed"]
    vals = [[],[1,5],[1,3],[1,101],[1,13],[1,10],[1,2],[1,94],[1,505],[1,333],[1,22],[1,11],[1]]
    test(funcs, vals)
    # 11,22,333,505,94,2,10,13,101,3