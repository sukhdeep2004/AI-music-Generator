from time import time
import requests
from urllib import response
from google import genai
from google.genai import types
import http.client
import json
import time 

def valid_music_type(argument):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="check if the music type is valid for the following input: " + str(argument) + "answer one word Yes or no",
        config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1
    )
    )
    return "yes" in response.text.lower().strip()


if __name__ == "__main__":
    api_key = input("Enter gemini your API Key: ")
    client = genai.Client(api_key=api_key)
    suno_api_key = input("Enter your Suno API Key: ")

    print("Please enter the music style you want to generate a music  for:")

    user_input = (input("Enter your Choice "))
    check = valid_music_type(user_input)
    if(check == False):
        print("Invalid choice. Please enter valid choice")
        while(valid_music_type(user_input) == False):
            user_input = (input("Enter your Choice "))
            if(valid_music_type(user_input) == True):
                break
            else:
                print("Invalid choice. Please enter valid choice")
    else:
        choice = "generate promt for suno api with music style  "+ str(user_input)+ "limit it to 25 words"+"""Use this JSON schema:
        promt: str"""
    
   
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=choice,
        config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1
    )
    )


    conn = http.client.HTTPSConnection("apibox.erweima.ai")
    payload = json.dumps({
    "prompt": response.text,
    "style": user_input,
    "title": "random",
    "customMode": True,
    "instrumental": True,
    "model": "V3_5",
    "callBackUrl": "https://api.example.com/callback"
    })
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization':f'Bearer {suno_api_key}'
    }
    conn.request("POST", "/api/v1/generate", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    print("🎵 API Response:", data)


    task_id = data.get("data", {}).get("taskId")
    if not task_id:
        print(" No taskId found in response.")
        exit()



