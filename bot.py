    from time import sleep
import tweepy
from apiclient.discovery import build

DEVELOPER_KEY = 'AIzaSyDEvwsT8LX-iRLbnBnZ84sEVlpwbMDyOO8'
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

FILE_NAME = 'last_seen.txt'
key = '1442332205301207051-FoO7ddnmyGMcd6dwgmawGU3jPupHdG'
secret = 'NpLlecuMrGLX330MJUYNxcVkFcsni6Upev9GMabhw8nGO'
consumer_key = 'SNLipBVF78vnhclWGFAMqBASt'
consumer_secret = 'WK9Q22AKVXmbgc9qj1crSNv6BUWX9JwXBu6fJ6V8XuRBSP0nbg'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)
lines = []
while True:
    tweets = api.mentions_timeline()
    ids = 'NR_jQoXXGpU'
    results = youtube.videos().list(id=ids, part='snippet').execute()
    for result in results.get('items', []):
        file = open('starship.txt', 'w')
        file.write(result['snippet']['description'])
        file.close()
    with open(FILE_NAME) as file_in:
        for line in file_in:
            lines.append(int(line))
    for tweet in tweets:
        if int(tweet.id) in lines:
            print("Already Replied to all tweets")
        else:
            if '#starship' in tweet.text.lower():
                file = open(FILE_NAME, 'a')
                file.write(str(tweet.id) + "\n")
                print(tweet.text)
                idofuser = tweet.id
                file2 = open('starship.txt', 'r')
                lineSTARSHIP = file2.readline()
                indexoffullstop = lineSTARSHIP.index(".")
                lineSTARSHIP = lineSTARSHIP[0:indexoffullstop]

                reply = "@" + tweet.user.screen_name + " " + lineSTARSHIP
                api.update_status(status=reply, in_reply_to_status_id=tweet.id)

                print("Reply #starship Successfull")
                file.close()
            else:
                file = open(FILE_NAME, 'a')
                file.write(str(tweet.id) + "\n")
                print(
                    "You need to Specify #Starsh    ip for daily updates on starship or #launch to get upcoming launch schedule"
                )
                file.close()
    file_in.close()

    sleep(30)
