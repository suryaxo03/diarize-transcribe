from pyannote.audio import Pipeline
from pyannote.core import SlidingWindow
from dotenv import load_dotenv
import os
from pydub import AudioSegment

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
AUDIO_PATH = "F:\\STT\\Speaker-Diarization\\car_audio.wav"
if not os.path.exists(AUDIO_PATH):
    raise FileNotFoundError(f"File {AUDIO_PATH} does not exist. Please check the filename and path.")

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1", use_auth_token=HF_TOKEN)

# Adjust sliding window for finer segmentation
pipeline.segmentation.sliding_window = SlidingWindow(duration=1.0, step=0.02)  # 1s window, 0.25s step

diarization = pipeline(
    AUDIO_PATH,
    min_speakers=1,
    max_speakers=10,
)

os.makedirs("F:\\STT\\Speaker-Diarization\\segments3", exist_ok=True)

audio = AudioSegment.from_wav(AUDIO_PATH)
segments = []
for idx, (turn, _, speaker) in enumerate(diarization.itertracks(yield_label=True)):
    start_ms = int(turn.start * 1000)
    end_ms = int(turn.end * 1000)
    segment_audio = audio[start_ms:end_ms]
    segment_audio.export(f"F:\\STT\\Speaker-Diarization\\segments3\\segment_{idx}_{speaker}.wav", format="wav")
    segments.append({
        "start": float(turn.start),
        "end": float(turn.end),
        "speaker": str(speaker)
    })

with open("F:\\STT\\Speaker-Diarization\\segments3.json", "w", encoding="utf-8") as f:
    import json
    json.dump(segments, f, ensure_ascii=False, indent=2)