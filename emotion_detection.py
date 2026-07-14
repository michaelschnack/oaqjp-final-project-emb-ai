import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends a text payload to the Watson NLP Emotion Predict service
    and returns the raw text response.
    """
    # Define the API endpoint URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set up the headers required by the Watson NLP service
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Format the input payload using the text passed to the function
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    try:
        # Send the POST request to the service
        response = requests.post(url, json=payload, headers=headers)
        
        # Return the text attribute of the response object
        return response.text
        
    except requests.exceptions.RequestException as e:
        # Return the error message if the request fails
        return f"Request failed: {e}"