import os
import requests

def Send_Slack_Notification(message):
    webhook_url = os.getenv('SLACK_WEBHOOK_URL')
    if webhook_url is None:
        raise ValueError("Slack Webhook URL is not set in the environment variables.")
    payload = {'text': message}
    response = requests.post(webhook_url, json=payload)
    return response.text

#send_slack_notification('complete')