from gtts import gTTS
import playsound

text ="지금부터 사용자의 모습과 노트북 화면이 녹화됩니다. 부정행위가 5회 이상 감지될 경우, 감독관의 요청에 따라야 합니다."

tts = gTTS(text=text, lang='ko')
tts.save("notice.mp3")

playsound.playsound("notice.mp3", True)