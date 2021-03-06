import sys
import logging

sys.path.insert(1, f"{__file__}/../../..")
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# export SLACK_API_TOKEN=xoxb-***
# python3 tests/samples/conversations/list_conversations.py

import os
from slack import WebClient

client = WebClient(token=os.environ["SLACK_API_TOKEN"])

response = client.conversations_list()

response = client.conversations_list(
    types="public_channel, private_channel"
)

channel_id = response["channels"][0]["id"]

response = client.conversations_info(
    channel=channel_id,
    include_num_members=1  # TODO: True
)
