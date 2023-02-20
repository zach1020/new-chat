# New Chat
## A script that allows you to have a conversation with ChatGPT in the terminal AND hear ChatGPT's responses spoken

### Install Dependencies
- `pip install openai gtts python-vlc pyaudio SpeechRecognition`
- You need to have VLC installed on your system to run this program
- You probably need to use Linux (tested on Ubuntu)

### Getting the API Key
- You need an OpenAI API key of your own for this program to work
- Start by going to https://openai.com/api/
- After setting up an account and generating an API key, add the API key to the `secret_key` variable in `keys.py` in the new-chat folder 


### How to Run
- Open terminal
- Navigate to the new-chat folder
- `python main.py`
- Enter your question in the prompt `> `
- Wait for ChatGPT to respond
- Repeat
- Exit the program with `CTRL-C`

### Increase/Decrease Possible Response Length
- You may want to increase or decrease the max token length to avoid a high usage rate, or in order to increase the length of the possible response size
- Change `max_token_length` in `chat.py` to meet your needs

### To Do
- Allow for continuous conversations
- Allow for the user to speak (speech to text -> ✅ChatGPT query/response -> ✅text to speech)
- Make it work on Mac and Windows
- Make it easier to exit the program (not just `CTRL-C`)
