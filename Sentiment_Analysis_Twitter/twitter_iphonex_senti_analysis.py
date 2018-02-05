#Importing the libraries
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Credentials
consumer_token = "ilpKS4eZXTKJICfoLE7D82uzv"
consumer_secret = "dLUFgkgrL75vtK6psWGydjXhEZXbR1sbiy3pWnnOhPiotJxWh0"
access_token="882160643222061057-91f8qeOUxenDRHuRirjxo5uMq1l1Ox0"
access_token_secret="468zbQ9PKyHPl6WhPZLZdtkKdNSHuGOifwkH78pqaz2RK"

class Listener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
 l = Listener()
 auth = OAuthHandler(consumer_token, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)
 stream = Stream(auth, l)
 
 stream.filter(track=['iPhoneX', '#iphonex'])
