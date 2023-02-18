from gtts import gTTS

import os 

import vlc
import time

def speak(my_text):
	language = 'en'

	my_obj = gTTS(text=my_text, lang=language, slow=False)

	my_obj.save('speak.mp3')

	p = vlc.MediaPlayer('speak.mp3')
	p.play()
	duration = p.get_length()
	time.sleep(duration / 1000) # duration in milliseconds