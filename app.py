from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import whisper
from transformers import pipeline
import os

app = FastAPI()

print("Loading AI Models... This might take a minute on first run.")
# Load speech-to-text model (using 'base' for high speed)
stt_model = whisper.load_model("base") 
# Load Hugging Face summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")
print("Models loaded successfully!")

@app.get("/")
async def serve_frontend():
    # Serves your custom HTML UI
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/generate-notes/")
async def generate_notes(file: UploadFile = File(...)):
    # 1. Save uploaded audio temporarily
    temp_audio_path = f"temp_{file.filename}"
    with open(temp_audio_path, "wb") as buffer:
        buffer.write(await file.read())
    
    try:
        # 2. Transcribe Audio (Speech-to-Text)
        result = stt_model.transcribe(temp_audio_path)
        transcript = result["text"]

        # 3. Generate Summary Notes (NLP)
        # Note: If audio is very short, max_length ensures it doesn't break
        input_length = len(transcript.split())
        max_len = min(130, max(30, input_length - 10)) 
        
        summary_output = summarizer(transcript, max_length=max_len, min_length=20, do_sample=False)
        summary = summary_output[0]['summary_text']

        return {"transcript": transcript, "summary": summary}
    
    finally:
        # 4. Cleanup the temporary audio file
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)