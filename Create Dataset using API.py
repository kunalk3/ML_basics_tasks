'''
We'll use the Twitch API provided by Free Code Camp https://wind-bow.glitch.me/, which makes the API use 
very easy and simple, to access a list of channels and its information.
'''


# Import necessary libraries
import pandas as pd
import requests
import json

url = "https://wind-bow.glitch.me/twitch-api/channels/freecodecamp"
JSONContent = requests.get(url).json()
content = json.dumps(JSONContent, indent = 4,sort_keys=True)
print(content)

# Output:
'''
{
    "_id": 79776140,
    "_links": {
        "chat": "https://api.twitch.tv/kraken/chat/freecodecamp",
        "commercial": "https://api.twitch.tv/kraken/channels/freecodecamp/commercial",
        "editors": "https://api.twitch.tv/kraken/channels/freecodecamp/editors",
        "follows": "https://api.twitch.tv/kraken/channels/freecodecamp/follows",
        "self": "https://api.twitch.tv/kraken/channels/freecodecamp",
        "stream_key": "https://api.twitch.tv/kraken/channels/freecodecamp/stream_key",
        "subscriptions": "https://api.twitch.tv/kraken/channels/freecodecamp/subscriptions",
        "teams": "https://api.twitch.tv/kraken/channels/freecodecamp/teams",
        "videos": "https://api.twitch.tv/kraken/channels/freecodecamp/videos"
    },
    "background": null,
    "banner": null,
    "broadcaster_language": "en",
    "created_at": "2015-01-14T03:36:47Z",
    "delay": null,
    "display_name": "FreeCodeCamp",
    "followers": 10122,
    "game": "Creative",
    "language": "en",
    "logo": "https://static-cdn.jtvnw.net/jtv_user_pictures/freecodecamp-profile_image-d9514f2df0962329-300x300.png",
    "mature": false,
    "name": "freecodecamp",
    "partner": false,
    "profile_banner": "https://static-cdn.jtvnw.net/jtv_user_pictures/freecodecamp-profile_banner-6f5e3445ff474aec-480.png",
    "profile_banner_background_color": null,
    "status": "Greg working on Electron-Vue boilerplate w/ Akira #programming #vuejs #electron",
    "updated_at": "2016-10-10T22:02:01Z",
    "url": "https://www.twitch.tv/freecodecamp",
    "video_banner": "https://static-cdn.jtvnw.net/jtv_user_pictures/freecodecamp-channel_offline_image-b8e133c78cd51cb0-1920x1080.png",
    "views": 163747
}
'''

# List of channels we want to access
channels = ["ESL_SC2", "OgamingSC2", "cretetion", "freecodecamp", "storbeck", "habathcx", "RobotCaleb", "noobs2ninjas",
            "ninja", "shroud", "Dakotaz", "esltv_cs", "pokimane", "tsm_bjergsen", "boxbox", "wtcn", "a_seagull",
           "kinggothalion", "amazhs", "jahrein", "thenadeshot", "sivhd", "kingrichard"]

channels_list = []
# For each channel, we access its information through its API
for channel in channels:
    JSONContent = requests.get("https://wind-bow.glitch.me/twitch-api/channels/" + channel).json()
    if 'error' not in JSONContent:
        channels_list.append([JSONContent['_id'], JSONContent['display_name'], JSONContent['status'],
                             JSONContent['followers'], JSONContent['views']])

dataset = pd.DataFrame(channels_list)
dataset.sample(5)
