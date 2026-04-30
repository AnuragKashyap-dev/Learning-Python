from gtts import gTTS
import os

text = "hello abhigyan garib hai"
tts = gTTS(text=text , lang='en')
tts.save("output.mp3")

os.system("start output.mp3")







