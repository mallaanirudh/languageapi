from flask import Flask, request, jsonify, render_template
import pyaudio
import wave
from langdetect import detect
from google.cloud import speech_v1 as speech
import os

app = Flask(__name__)

# Ensure Google Cloud credentials are set
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\malla\Downloads\silicon-vertex-439907-p1-9f214af6b2e8.json"
#Ensure that when you deploy use the path that exist on the local machine after you download the json file from google account.
#the above path is my path on my local machine
# Function to record audio from the microphone
def record_audio(filename, duration=10):
    chunk = 1024
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1  # Mono
    fs = 16000  # Sampling frequency
    p = pyaudio.PyAudio()

    print("Recording...")
    stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
    frames = []

    for _ in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Recording complete.")

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to transcribe audio to text using Google Speech-to-Text API
def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    with wave.open(audio_file, "rb") as wf:
        audio_data = wf.readframes(wf.getnframes())
    
    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        alternative_language_codes=["hi-IN", "zh-CN", "fr-FR", "de-DE", "ar-SA", "es-ES", "te-IN"],
    )

    response = client.recognize(config=config, audio=audio)

    transcriptions = []
    for result in response.results:
        transcriptions.append(result.alternatives[0].transcript)
    
    return " ".join(transcriptions)

# Flask route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to detect language
@app.route('/detect_language', methods=['POST'])
def detect_language_api():
    duration = request.json.get("duration", 10)  # Default to 10 seconds
    
    # Step 1: Record audio from the microphone
    audio_file = "recorded_audio.wav"
    record_audio(audio_file, duration)

    # Step 2: Transcribe the recorded audio
    transcribed_text = transcribe_audio(audio_file)

    if transcribed_text:
        # Step 3: Detect the language from the transcribed text
        language = detect(transcribed_text)
        return jsonify({
            "transcribed_text": transcribed_text,
            "detected_language": language
        })
    else:
        return jsonify({"error": "No text detected in the audio."}), 400

if __name__ == '__main__':
    app.run(debug=True)

