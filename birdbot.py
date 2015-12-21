import tweepy
from bs4 import BeautifulSoup
import urllib
import os

# auth
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#get image url
url = "https://birdshow.dfkt.tk/getimage.php"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
link = "https://birdshow.dfkt.tk/" + soup.get_text()
#print(link)

#download image
download_img = "./img.jpg"
urllib.urlretrieve(link, download_img)

#post tweet
status = "#birdbot"
api.update_with_media(download_img, status=status)

#delete downloaded image
os.remove(download_img)

#followers/friends
#screen_name = api.me().screen_name
bot = api.me().id
followers = api.followers_ids(bot)
friends = api.friends_ids(bot)

#unfollow back
for friend in friends:
    if friend not in followers:
        api.destroy_friendship(friend)

#follow back
for follower in followers:
    if follower not in friends:
        api.create_friendship(follower)
        friends.append(follower)
