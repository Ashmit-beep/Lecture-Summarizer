import whisper

model = whisper.load_model("base")

result = model.transcribe("audio.m4a")
print("Transcript: ", result["text"]) 