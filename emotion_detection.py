import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.p.cloud.ibm.com/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"Letters-Id": "watson-emotion-v1-emotion", "Content-Type": "application/json"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    if not text_to_analyze:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    response = requests.post(url, json=myobj, headers=header )
    
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': emotions['anger'], 'disgust': emotions['disgust'], 'fear': emotions['fear'],
        'joy': emotions['joy'], 'sadness': emotions['sadness'], 'dominant_emotion': dominant_emotion
    }