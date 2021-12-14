# A sample Python script for uploading an image to Slack channel

This is minimal example of python script,
which simply uploads an image to Slack channel.

## Overview

This script works as a simplest Bot and posts message to the channel,
using authorization token (called Bot Token, in Slack), and Channel ID.

## Preparation

It is recommended to read instruction of Slack - [Getting started with Bolt for Python over HTTP](https://slack.dev/bolt-python/tutorial/getting-started-http).

### 1. At Slack Website: Crate an Application and Token

1. Create an Application with any name.
1. Add `files:write` scope to the Bot Token Scope (permission).
    - Please refer [manifest.yml](manifest.yml) for detail about manifest which was used to test this script.
1. Install the Application to the Workspace at "OAuth & Permissions" page, as shown in the instruction.
    Then you will get _Bot User OAuth Token_, which is needed to give permission to the script.

### 2. At Your Slack Client: Add the Application to the Channel and Get Channel ID

1. Optional) if you are going to use private channel to post images,
    you need to add the Application to members of the channel and give permission to post messages to the channel.
    1. In Slack application, please open _Channel Details_.
    1. On _Integration_ tab, add application installed in previous step.
1. Open _Channel Details_, in slack application and retrieve Channel ID, which is written at last part of the page.

1st step can be skipped when you are going to use public channel in the workspace.

### 3. At Your Python Environment: Setup Scripts

1. Please install dependent libraries.

    ```
    pip install -r requirements.txt
    ```

1. Put a configuration file `config.json` on the directory to run the script. This configuration contains:
    * Bot Token generated in step 1.
    * Channel ID retrieved in step 2.
    * The configuration file looks like following:

        ```
        {
            "bot_token": "xoxb-xxxxxxxxxxxxx-yyyyyyyyyyyyy-zzzzzzzzzzzzzzzzzzzzzzzz",
            "channel_id": "12345678901"
        }
        ```

## Usage

Simply post an image:

```
python slack_photo_uploader.py YOUR_IMAGE
```

Or post an image with messages:

```
python slack_photo_uploader.py YOUR_IMAGE -m "Your message"
```

## Reference

* [files.upload](https://api.slack.com/methods/files.upload/code) -- sample code for the Web API.
