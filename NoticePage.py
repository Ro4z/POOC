from gtts import gTTS
import playsound

text ="지금부터 사용자의 모습과 노트북 화면이 녹화됩니다. 부정행위가 5회 이상 감지될 경우, 감독관의 요청에 따라야 합니다.  부정 행위 판단 기준은 다음과 같습니다." \
      "첫째, alt, window, control key등의 특수키를 눌렀을 경우.  둘째, 눈이 노트북화면을 향하지 않고 왼쪽, 오른쪽을 향하는 경우."

tts = gTTS(text=text, lang='ko')
tts.save("notice.mp3")

playsound.playsound("notice.mp3", True)