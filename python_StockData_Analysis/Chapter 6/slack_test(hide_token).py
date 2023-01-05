from slacker import Slacker

myToken = "token"

import requests

def post_message(token, channel, answer):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": answer}
    )

# slack.chat.post_message(channel, answer)  // slack.chat.post_message -> post_message 으로 대체
post_message(myToken, 'stock', 'It\'s too hard')


