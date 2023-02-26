
# Question 5b

class Tweet:
    def __init__(self, text):
        self.tweet_text = text
        
        if len(self.tweet_text) > 280:
            self.tweet_text = self.tweet_text[:280]
      
            
    def get_text(self):
        return self.tweet_text
    
    def set_text(self, text):
        self.tweet_text = text
        if len(self.tweet_text) > 280:
            self.tweet_text = self.tweet_text[:280]
            
    def get_retweets(self):
        return self.retweets
    
    def set_retweets(self, retweets):
        self.retweets = retweets
        if self.retweets < 0:
            self.retweets = 0
            
    def get_likes(self):
        return self.likes
    
    def set_likes(self, likes):
        self.likes = likes
        if self.likes < 0:
            self.likes = 0
            
    def get_touches(self):
        return self.touches
    
    def set_touches(self, touches):
        self.touches = touches
        if self.touches < 0:
            self.touches = 0
            
    def __str__(self):
        return self.tweet_text
    
    def total_impressions(self):
        return self.retweets + self.likes + self.touches
    
    def pretty_print(self):
        return print(f"Tweet: {self.tweet_text} Retweets: {self.retweets} Likes: {self.likes} Touches: {self.touches} Impressions: {self.total_impressions()}")


# Test the class
tweet1 = Tweet("This is an example tweet.")
tweet1.set_likes(12)
tweet1.set_retweets(17)
tweet1.set_touches(200)
print(tweet1.pretty_print())


