from chat import chat
from tts import speak
from stt import stt

# main.py
''' Old main function
def main():
	prompt = ''
	while prompt != 'quit':
		prompt = input('> ')
		speak(chat(prompt))
'''

def main():
	while True:
		prompt = stt()
		speak(chat(prompt))


main()
