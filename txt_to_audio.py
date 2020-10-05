from gtts import gTTS
from playsound import playsound

audio = "audio.mp3"
language = "en"
inp = input("Enter text you want to convert in audio...")
clip = gTTS(text=inp, lang=language, slow=False)

clip.save(audio)
playsound(audio)