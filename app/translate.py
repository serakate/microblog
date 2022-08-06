import json

import requests
from flask import current_app
from flask_babel import _

url = "https://microsoft-translator-text.p.rapidapi.com/translate"

def translate(text, source_language, dest_language):
    if 'X_RAPIDAPI_KEY' not in current_app.config or not current_app.config['X_RAPIDAPI_KEY']:
        return _('Error: the translation service is not configured.')
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": current_app.config['X_RAPIDAPI_KEY'],
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
        }
    querystring = {
        "to[0]": dest_language,
        "api-version":"3.0",
        "from": source_language,
        "profanityAction":"NoAction",
        "textType":"plain"
        }
    response = requests.request("POST", url, json=[{"Text": text}], headers=headers, params=querystring)
    if response.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(response.text)[0]["translations"][0]['text']

# payload = [{"Text": "I would really like to drive your car around the block a few times."}]
# response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
# [
#     {
#         "detectedLanguage":
#             {
#                 "language":"en",
#                 "score":1.0
#             },
#         "translations":
#             [
#                 {
#                     "text":"Мне бы очень хотелось несколько раз проехать на вашей машине по кварталу.",
#                     "to":"ru"
#                 }
#             ]
#     }
# ]
