# Question 5a
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
        
    def __str__(self):
        return self.tweet_text
    
    def tweet_text(self):
        return self.tweet_text


# Test the class
tweet = Tweet("Hello world!")
print(f"Text in tweet: {tweet.tweet_text}")


