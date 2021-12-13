import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

logger = logging.getLogger(__name__)

def load_config(cfg_file):
    with open(cfg_file) as f:
        cfg = json.load(f)
        return cfg

def upload(opt):
    filename = opt.get('filename')
    cfg = load_config(opt.get('config'))
    channel_id = cfg.get('channel_id')
    message = opt.get('message')
    # ID of channel that you want to upload file to.
    client = WebClient(token=cfg.get('bot_token'))

    try:
        # Call the files.upload method using the WebClient
        # Uploading files requires the `files:write` scope
        result = client.files_upload(
            channels=channel_id,
            initial_comment=message,
            file=filename
        )
        # Log the result
        logger.info(result)

    except SlackApiError as e:
        logger.error("Error uploading file: {}".format(e))

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Script to upload an image to Slack.')
    parser.add_argument('filename',
            help='filename of the image to upload')
    parser.add_argument('-c', '--config',
            help='configuration JSON file which stores Bot Token and Channel ID.', default='config.json')
    parser.add_argument('-m', '--message', 
            help='text message sent with the image.')
    opt = vars(parser.parse_args())
    upload(opt)
