import speech_recognition as sr  # For speech recognition


def stt():

	r = sr.Recognizer() 

	mic = sr.Microphone()

	audio_text = "" 

	with mic as source:
		# r.adjust_for_ambient_noise(source) # Uncomment this to avoid detecting ambient noise
		audio = r.listen(source)
		audio_text = r.recognize_google(audio)

	#print(audio_text)
	return audio_text
