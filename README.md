# A sample Python script for uploading an image to Slack channel

This is minimal example of python script,
which simply uploads an image to Slack channel.

## Overview

This script works as a simplest Bot and posts message to the channel,
using authorization token (called Bot Token, in Slack), and Channel ID.

## Preparation

Please follow instruction of Slack - [Getting started with Bolt for Python over HTTP](https://slack.dev/bolt-python/tutorial/getting-started-http).

### Install Library

Please install dependent libraries.

```
pip install -r requirements.txt
```

### Optional Step

1. Create Workspace to test this script.
    This can be done by clicking a link shown in above mentioned instruction.
    Or, please click [This Link](https://slack.com/get-started#create).

### Main Steps

1. Create and Application with any name.
1. Add Bot permission to `files:write` and `chat:write`.
1. Install the Application to the Workspace, as shown in the instruction.
1. (Optional) If you are going to use private channel to post images, add permission to the installed application.
    1. In Slack application, please open _Channel Details_.
    1. On _Integration_ tab, add application installed in previous step.
1. Open _Channel Details_, in slack application and retrieve Channel ID.
1. Setup configuration file `config.json`. This configuration contains:
    * Bot Token generated in step 3.
    * Channel ID retrieved in step 5.

## Usage

```
python slack_photo_uploader.py YOUR_IMAGE
```

## Reference

* [files.upload](https://api.slack.com/methods/files.upload/code) -- sample code for the Web API.
