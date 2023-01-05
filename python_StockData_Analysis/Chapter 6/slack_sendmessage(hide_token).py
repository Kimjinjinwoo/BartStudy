token = 'token'
import requests
from slacker import Slacker
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


client = WebClient(token)

markdown_text = '''
This message is plain.
*This message is bold.*
'This message is code.'
_This message is italic._
~This message is strike.~
'''

attach_dict = {
        'color'         :'#ff0000',
        'author_name'   :'Kimjinjinwoo',
        'author_link'   :'github.com/Kimjinjinwoo',
        'title'         :'오늘의 증시 KOSPI',
        'title_link'    :'http://finance.naver.com/sise/sise_index.nhn?code=KOSPI',
        'text'          :'2,330.98 △8.66 (+0.37%)',
        'image_url'     :'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png'
}


attachList = [attach_dict]


try:
        result = client.chat_postMessage(
                channel='stock',
                text=markdown_text,
                attachments=attachList)          
        print(result)


except SlackApiError as e:
        print(f"Error: {e}")
