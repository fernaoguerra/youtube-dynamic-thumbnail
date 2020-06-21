import os
import googleapiclient.discovery
from apiclient import discovery
from dotenv import load_dotenv

load_dotenv()

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
