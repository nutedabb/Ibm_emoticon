import requests
import json

def emotion_detector(text_to_analyze):
    """ this fuction checks the emotion of a given 
    word and returns a dictionary
    """
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=Input_json, headers = Headers)
    cleaned_response = json.loads(response.text)
    cleaned_response = cleaned_response['emotionPredictions'][0]["emotion"]
    dominant_emotion = ""
    for k,v in cleaned_response.items():
        if max(cleaned_response.values()) == v:
            dominant_emotion = k
            

    final_response = {**cleaned_response,"dominant_emotion":dominant_emotion}
    print(final_response)
   

