from gtts import gTTS
import playsound

text ="사랑햄"

tts = gTTS(text=text, lang='ko')
tts.save("notice.mp3")

playsound.playsound("notice.mp3", True)