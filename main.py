from gtts import gTTS
import os

x = "Слава яйцам!"
audio = gTTS(text=x, lang='ru', slow=True)
audio.save("audio.mp3")
os.system("start audio.mp3")
