import os
import googleapiclient.discovery
from apiclient import discovery
from dotenv import load_dotenv
# from google.cloud import language_v1
# from google.cloud.language_v1 import enums

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account-file.json"

def get_comments():
    youtube = discovery.build("youtube", "v3", developerKey=os.getenv("GOOGLE_API_KEY"))
    request = youtube.commentThreads().list(
        part="Snippet",
        videoId="_P0VUM28Qsw"
    )
    response = request.execute()
    # print(response)
    comments = response['items']
    for comment in comments:
        c = (comment['snippet']['topLevelComment']['snippet']['textOriginal'])
        sample_analyze_sentiment(c)

def get_views():
    youtube = discovery.build("youtube", "v3", developerKey=os.getenv("GOOGLE_API_KEY"))
    request = youtube.videos().list(
        part="statistics",
        id="Al5W-wZ2FOs"
    )
    response = request.execute()  
    print(response)
    views = response['items'][0]['statistics']['viewCount']
    print (views)
    return views
    
    
def get_youtube_subscribers():
    youtube = discovery.build("youtube", "v3", developerKey=os.getenv("GOOGLE_API_KEY"))
    request = youtube.channels().list(
        part="Snippet,statistics",
        id="UC0reVIjVRp1i50qiY9lIp4A"
    )
    response = request.execute()  
    subscriber_count = response['items'][0]['statistics']['subscriberCount']
    print (subscriber_count)
    return subscriber_count
    


get_views()
