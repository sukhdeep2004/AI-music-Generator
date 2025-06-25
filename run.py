import requests
from urllib import response
from google import genai
from google.genai import types
import http.client
import json

client = genai.Client(api_key="AIzaSyBM24O8IBcbrTMU9GY8Euu_y_E4YInKqkM")
def valid_music_type(argument):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="check if the music type is valid for the following input: " + str(argument) + "answer one word Yes or no",
        config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1
    )
    )
    print(response.text.lower().strip())
    return "yes" in response.text.lower().strip()


if __name__ == "__main__":
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
    print(response.text)


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
    'Authorization': 'Bearer ebb91a8ee28b4b693350eee0d349cdc7'
    }
    conn.request("POST", "/api/v1/generate", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    print("🎵 API Response:", data)

    # Extract audio URL (update the key to match the real one)
    audio_url = data.get("audioUrl")

    if audio_url:
        print(f"Audio URL: {audio_url}")
        audio_response = requests.get(audio_url)

        if audio_response.status_code == 200:
            with open("generated_music.mp3", "wb") as f:
                f.write(audio_response.content)
            print(" Saved audio to 'generated_music.mp3'")
        else:
            print(f" Failed to download audio. HTTP {audio_response.status_code}")
    else:
        print(" No audio URL found in the response.")




