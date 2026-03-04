# Lecture Voice-to-Notes Generator 🎙️📝

A full-stack artificial intelligence application designed to seamlessly
convert spoken lectures into concise, structured study notes. This
project bridges the gap between passive listening and active studying by
automating the transcription and summarization of educational audio
content.

Developed as a Capstone Project to provide an accessible, on-demand
academic tool for students.

------------------------------------------------------------------------

## ✨ Features

-   **Multi-Format Audio Ingestion:** Supports `.mp3`, `.wav`, and
    `.m4a` Apple audio files.
-   **High-Fidelity Transcription:** Utilizes OpenAI's Whisper model for
    accurate, offline speech-to-text conversion.
-   **Smart Summarization:** Employs the Hugging Face
    `facebook/bart-large-cnn` NLP model to distill lengthy transcripts
    into core educational concepts.
-   **Auto-Truncation:** Safely handles large audio files by dynamically
    chunking and truncating text to prevent memory overload.
-   **Modern Web UI:** A responsive, dark-theme glass-morphism interface
    with drag-and-drop file support.

------------------------------------------------------------------------

## 🛠️ Technology Stack

**Frontend** - HTML5 - CSS3 - JavaScript

**Backend** - Python - FastAPI - Uvicorn (ASGI Server)

**Machine Learning / AI** - `openai-whisper` (Speech-to-Text) -
`transformers` (NLP Pipeline) - `torch` (PyTorch Framework for efficient
CPU/GPU inference)

------------------------------------------------------------------------

## ⚙️ Prerequisites

Before running the application, ensure you have the following installed
on your system:

1.  **Python 3.8+**
2.  **FFmpeg** -- Required by Whisper to process audio files (especially
    `.m4a`).

### Windows Installation

Open Command Prompt as Administrator and run:

    winget install ffmpeg

------------------------------------------------------------------------

## 🚀 Installation & Setup

### 1. Clone or Download the Repository

Navigate to your project directory (e.g., `Aicte-project`).

### 2. Install Python Dependencies

Make sure `requirements.txt` exists in the project directory, then run:

    pip install -r requirements.txt

### 3. Run the Backend Server

Start the FastAPI application using Uvicorn:

    uvicorn app:app --reload

**Note:**\
The first time you run the application and process an audio file, it
will take a few minutes to download the Whisper and BART AI models to
your local cache. Subsequent runs will be significantly faster.

------------------------------------------------------------------------

## 💻 Usage

1. Navigate to the **Live Demo** or open your local browser:  
   👉 https://huggingface.co/spaces/Vijay1108/language-to-text  
   or  
   👉 http://127.0.0.1:8000

2. Drag and drop a lecture audio file (`.mp3`, `.wav`, or `.m4a`) into the upload area.

3. Click **Generate Smart Notes**.

4. Wait for the AI models to process the audio.

5. The **raw transcript** and **AI-generated summary** will automatically appear on the screen.

------------------------------------------------------------------------

## 📂 Project Structure

    📦 AI-Study-Buddy
     ┣ 📜 app.py               # FastAPI backend and AI pipeline logic
     ┣ 📜 index.html           # Frontend user interface
     ┣ 📜 requirements.txt     # Python package dependencies
     ┗ 📜 README.md            # Project documentation

------------------------------------------------------------------------

## 🎓 Project Goal

The goal of this project is to help students convert long lecture
recordings into concise, structured notes automatically. By combining
**speech recognition** with **AI-powered summarization**, the platform
transforms passive lecture listening into **efficient study material
generation**.

------------------------------------------------------------------------

## 📜 License

This project is created for **educational and academic purposes** as
part of a capstone project.
