#  1st program
from playsound import playsound 
from gtts import gTTS
from AudioResponse import a
audio = 'speech.mp3'
language = 'en'
print("enter your text")
# b = input()
c = a[b]
Text = c
sp = gTTS(text=Text, lang=language, slow=False)
sp.save(audio)
playsound(audio)
