# languageapi
# Voice Language Detection API with Flask

This project provides a Flask-based API that records audio from the microphone, transcribes it using Google Cloud Speech-to-Text, and detects the language of the transcribed text using the `langdetect` library.

## Prerequisites

Before running the application, ensure you have the following installed:

* **Python 3.6+**
* **pip** (Python package installer)
* **Google Cloud SDK** (if deploying to Google Cloud)
* **Google Cloud Service Account Credentials:**
    * You'll need a Google Cloud Platform (GCP) project with the Speech-to-Text API enabled.
    * Download the service account credentials JSON file and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the file's path.
* **pyaudio:** for recording audio.
* **wave:** for saving audio files.
* **langdetect:** for language detection.
* **google-cloud-speech:** for speech-to-text.
* **Flask:** for the web application.

## Installation

1.  **Clone the repository (if applicable):**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install the required Python packages:**

    ```bash
    pip install Flask pyaudio wave langdetect google-cloud-speech
    ```

3.  **Set Google Cloud Credentials:**

    * Download your Google Cloud service account JSON file.
    * Replace `"fewhoiejoifj######################"` in the python code, with the correct path to your json file.
    * Alternatively, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable:

    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
    ```
    * On windows, replace export with set.

4.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    The application will start running on `http://127.0.0.1:5000/`.

## Usage

1.  **Access the web interface:**
    * Open your web browser and navigate to `http://127.0.0.1:5000/`.
    * Ensure that an index.html file exists in the templates folder. The index.html file, should have client side javascript that records audio, and then sends it to the /detect_language endpoint.
2.  **Record audio:**
    * The web page should provide a button or interface to start recording audio from your microphone.
    * The audio will be recorded for a specified duration (default is 10 seconds).
3.  **Detect language:**
    * After recording, the audio is sent to the `/detect_language` API endpoint.
    * The API transcribes the audio and detects the language.
    * The result (transcribed text and detected language) is displayed on the web page.

## API Endpoint

* **`/detect_language` (POST):**
    * Records audio, transcribes it, and detects the language.
    * **Request:**
        * JSON payload with an optional `duration` field (in seconds).
    * **Response:**
        * JSON object with `transcribed_text` and `detected_language` fields.
        * Returns an error message if no text is detected

## Prerequisites

Before running the application, ensure you have the following installed:

* **Python 3.6+**
* **pip** (Python package installer)
* **Google Cloud SDK** (if deploying to Google Cloud)
* **Google Cloud Service Account Credentials:**
    * You'll need a Google Cloud Platform (GCP) project with the Speech-to-Text API enabled.
    * Download the service account credentials JSON file and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the file's path.
* **pyaudio:** for recording audio.
* **wave:** for saving audio files.
* **langdetect:** for language detection.
* **google-cloud-speech:** for speech-to-text.
* **Flask:** for the web application

## File Structure

voice-language-detection/
├── app.py
├── templates/
│   └── index.html
└── README.md
`app.py`: The main Flask application.
* `templates/index.html`: The HTML page for the web interface.

## Notes

* Ensure your microphone is properly configured.
* The accuracy of language detection depends on the clarity of the audio and the complexity of the spoken language.
* For production, ensure to remove debug=True from app.run()
* Error handling should be expanded.
* The index.html file would need to be created, and contain the javascript to record audio, and send it to the flask backend.
