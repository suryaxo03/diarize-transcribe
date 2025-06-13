import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

SEGMENTS_JSON = "F:\\STT\\Speaker-Diarization\\segments1.json"
SEGMENTS_DIR = "F:\\STT\\Speaker-Diarization\\segments1"
TRANSCRIPTIONS_JSON = "F:\\STT\\Speaker-Diarization\\segment_transcriptions1.json"

# Load diarization segments
with open(SEGMENTS_JSON, "r", encoding="utf-8") as f:
    segments = json.load(f)

results = []
for idx, seg in enumerate(segments):
    filename = f"segment_{idx}_{seg['speaker']}.wav"
    file_path = os.path.join(SEGMENTS_DIR, filename)
    print(f"Transcribing {file_path} ...")
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="gpt-4o-transcribe",  # or "gpt-4o-transcribe" if available
            language="en"       # Tamil
        )
    results.append({
        "segment": idx,
        "speaker": seg["speaker"],
        "start": seg["start"],
        "end": seg["end"],
        "text": transcription.text
    })

# Save all transcriptions
with open(TRANSCRIPTIONS_JSON, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Transcribed {len(results)} segments. Results saved to {TRANSCRIPTIONS_JSON}")