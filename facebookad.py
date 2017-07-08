import sys
import os
import json

from facebookads.api import FacebookAdsApi
from facebookads.session import FacebookSession
from facebookads.adobjects.advideo import AdVideo

#FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)


"""
Upload a video to adaccount
"""


sdk_path = os.path.abspath(os.path.join(__file__, os.pardir))
sys.path.insert(1, sdk_path)

config_filename = os.path.join(sdk_path, './config.json')

config_file = open(config_filename)
config = json.load(config_file)
config_file.close()

### Setup session and api objects
session = FacebookSession(
    config['app_id'],
    config['app_secret'],
    config['access_token'],
)

FacebookAdsApi.set_default_api(FacebookAdsApi(session))

if __name__ == '__main__':
    # create video object
    video = AdVideo(parent_id=config['act_id'])

    video_path = os.path.join(
        os.path.dirname(__file__),
        'test.mov'
        #'sample.mp4'
    )

    # set video fields
    video[AdVideo.Field.filepath] = video_path

    # remote create
    video.remote_create()
    video.waitUntilEncodingReady(2, 3600)

    print(video)

