import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text_json = { "raw_document": { "text": text_to_analyze } }

    raw_response = requests.post(url, json = input_text_json, headers = headers)
    response = json.loads(raw_response.text)            
    emotions_dict = response['emotionPredictions'][0]['emotion']
    max_emotion = max(emotions_dict, key=emotions_dict.get)
    emotions_dict['dominant_emotion'] = max_emotion

    return emotions_dict