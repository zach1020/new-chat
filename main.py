from chat import chat
from tts import speak

# main.py

def main():
	prompt = ''
	while prompt != 'quit':
		prompt = input('> ')
		speak(chat(prompt))

main()