class Twitter:

    def __init__(self):
        self.d_friends = defaultdict(set)
        # {user:[follow1, follow2...]}
        self.d_posts = defaultdict(list)
        # {user: [post1, post2,...]}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.d_posts[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        st = []
        for idx in self.d_friends[userId]:
            st.extend(self.d_posts[idx])
        st.extend(self.d_posts[userId])
        st.sort(reverse=True)
        ans = []
        length = 10
        if len(st) < 10:
            length = len(st)
        for i in range(length):
            ans.append(st[i][1])
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.d_friends[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.d_friends[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)