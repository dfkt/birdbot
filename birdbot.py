import tweepy
import urllib
from bs4 import BeautifulSoup
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
for script in soup(["script", "style"]):
    script.extract()

link = "https://birdshow.dfkt.tk/" + soup.get_text()
#print(link)

#download image
urllib.urlretrieve(link, "./img.jpg")

#post tweet
download = "./img.jpg"
status = "#birdbot"
api.update_with_media(download, status=status)

#delete downloaded image
os.remove("./img.jpg")

#follow back
for follower in tweepy.Cursor(api.followers).items(2):
    follower.follow()
    #print follower.screen_name

#unfollow back
followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)
for f in friends:
    if f not in followers:
        api.destroy_friendship(f)
