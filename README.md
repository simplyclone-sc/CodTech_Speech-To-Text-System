# 🗣️ Speech-to-Text System using Wav2Vec2

This is a basic speech-to-text system I built as part of my **CodTech AI Internship (Task-2)**. The goal was to create a simple yet functional program that can **record voice through the microphone** and **convert it to text instantly**, using a pre-trained deep learning model.

---

## 🚀 What it Does

- 🎙️ Records your voice in real-time (5 seconds)
- 🧠 Uses `Wav2Vec2` from HuggingFace to process the audio
- 📄 Prints the transcribed text output

---

## 📚 Technologies Used

- Python 3.x
- [Transformers (HuggingFace)](https://huggingface.co/transformers/)
- Wav2Vec2 Pretrained Model: `facebook/wav2vec2-base-960h`
- Libraries: `sounddevice`, `scipy`, `librosa`, `torch`

---

## 🛠️ How It Works (Behind the Scenes)

1. **Record Voice** – The script captures 5 seconds of your voice using your microphone and saves it as `live_audio.wav`.
2. **Load Audio** – Audio is loaded and resampled to 16000 Hz using `librosa`.
3. **Tokenize Input** – The audio waveform is tokenized for the model.
4. **Model Inference** – The Wav2Vec2 model transcribes the tokenized audio.
5. **Text Output** – The decoded text is printed to the console.

---

## 💻 How to Run

1. **Clone this repository** or download the project folder.  
2. Make sure Python is installed (3.8 or above recommended).  
3. Install dependencies:  

```bash
pip install -r requirements.txt
```
4. Run the main script:

```bash
python speech_to_text.py
```
5. Speak when prompted, and your transcribed text will appear right after.


## ✅ Task-2 Internship Goal

“Build a basic speech-to-text system using pre-trained models like SpeechRecognition or Wav2Vec.”

This project meets that goal using Wav2Vec2, which provides deep learning-based transcription with good accuracy.

---

## 📁 Project Structure
<pre>
SpeechToTextSystem/
│
├── speech_to_text.py        # Main script
├── requirements.txt         # Required libraries
├── .gitignore               # Ignore wav and cache files
└── live_audio.wav           # Auto-generated at runtime
</pre>

---

## 📌 Notes
• Works best with clear audio and little background noise.
• live_audio.wav is automatically created on every run — no need to upload it to GitHub.

---

##  🙋‍♂️ Made By

### 👤 Author
Anas Bin Fares Lardi  
GitHub 👉🏻 https://github.com/simplyclone-sc/    
LinkedIn 👉🏻 https://www.linkedin.com/in/anas-lardi-b41a16375/    
