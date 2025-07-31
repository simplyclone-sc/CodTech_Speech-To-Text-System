import torch
import sounddevice as sd
from scipy.io.wavfile import write
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

# Load model and tokenizer once
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Record audio
duration = 5  # seconds
sample_rate = 16000
print("🎙️ Speak now...")
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()
write("live_audio.wav", sample_rate, recording)
print("✅ Audio recorded. Transcribing...")

# Load and process the audio
audio, sr = librosa.load("live_audio.wav", sr=16000)
input_values = tokenizer(audio, return_tensors="pt", padding="longest").input_values

# Transcribe
with torch.no_grad():
    logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcription = tokenizer.decode(predicted_ids[0])

# Output result
print("📝 Transcription:", transcription)