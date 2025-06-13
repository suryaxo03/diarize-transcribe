# Speaker Diarization & Transcription Pipeline

---

## 🗝️ Key Libraries Used

- <span style="color:#3572A5; font-weight:bold">pyannote.audio</span> — Speaker diarization (Hugging Face)
- <span style="color:#FADA5E; font-weight:bold">pydub</span> — Audio file manipulation
- <span style="color:#4B8BBE; font-weight:bold">python-dotenv</span> — Environment variable management
- <span style="color:#F7B731; font-weight:bold">openai</span> — Whisper API for transcription
- <span style="color:#E34C26; font-weight:bold">ffmpeg</span> — Audio backend for pydub (system dependency)

---

## File Overview

- `speaker_diarization.py`: Performs speaker diarization and splits the audio into per-speaker segments.
- `transcribe_segments.py`: Transcribes each segment using the OpenAI API and saves the results.
- `segmentsX/`: Folders containing the extracted audio segments (one `.wav` per segment).
- `segmentsX.json`: JSON files with segment metadata (start, end, speaker).
- `segment_transcriptions.json`: Final transcription results for all segments.

---

## Setup

### 1. Clone the repository and install dependencies

```powershell
pip install pyannote.audio pydub python-dotenv openai
```
- You also need [ffmpeg](https://ffmpeg.org/download.html) installed and in your PATH for `pydub` to work with audio files.

### 2. Environment Variables

Create a `.env` file in the `Speaker-Diarization` directory with:
```
HF_TOKEN=your_huggingface_token
OPENAI_API_KEY=your_openai_api_key
```
- Get your Hugging Face token from https://huggingface.co/settings/tokens
- Get your OpenAI API key from https://platform.openai.com/api-keys

---

## Usage

### 1. Speaker Diarization & Segment Extraction

Edit `AUDIO_PATH` in `speaker_diarization.py` to point to your input `.wav` file.

Run:
```powershell
python speaker_diarization.py
```
- This will create a folder (e.g., `segments3/`) with one `.wav` file per segment and a `segments3.json` file with segment info.

### 2. Transcribe Segments

Edit `SEGMENTS_JSON` and `SEGMENTS_DIR` in `transcribe_segments.py` to match your segment output.

Run:
```powershell
python transcribe_segments.py
```
- This will create `segment_transcriptions.json` with the transcription for each segment.

---

## Output Example

- `segments3.json`:
```json
[
  { "start": 5.18, "end": 19.50, "speaker": "SPEAKER_02" },
  { "start": 9.21, "end": 9.46, "speaker": "SPEAKER_00" },
  ...
]
```
- `segment_transcriptions.json`:
```json
[
  { "segment": 0, "speaker": "SPEAKER_02", "start": 5.18, "end": 19.50, "text": "..." },
  ...
]
```

---

## Customization
- Adjust `min_speakers`, `max_speakers`, and `SlidingWindow` parameters in `speaker_diarization.py` for your audio.
- Change output directories as needed.

---

## Troubleshooting
- **FileNotFoundError**: Check your audio file path and segment directory.
- **API errors**: Ensure your Hugging Face and OpenAI tokens are valid and not rate-limited.
- **Large files**: Exclude `.wav` and segment folders from git using `.gitignore`.

---

## License
This project is for research and educational purposes. See individual model licenses for pyannote and OpenAI Whisper.
