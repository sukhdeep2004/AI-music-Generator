# 🎶 AI-Powered Music Generator

A Python-based command-line tool that lets you generate music using **Google Gemini (genai)** and **Suno API**. Users input a music style (e.g., "jazz", "lo-fi", "classical"), and the app uses Gemini to validate the style and generate a creative music prompt. It then sends this prompt to Suno’s API to generate music.

---

## 🚀 Features

- ✅ Validate user-provided music styles using Gemini (Google AI)
- 🧠 Automatically generate a 25-word music prompt for the selected style
- 🎼 Send the prompt to the Suno API to create instrumental music
- 📡 Get real-time task status and print the API response

---

## 🛠️ Requirements

- Python 3.8+
- Google Gemini API key (https://makersuite.google.com/app)
- Suno API key (from [apibox.erweima.ai](https://apibox.erweima.ai/))

Install dependencies:

```bash
pip install google-generativeai requests
