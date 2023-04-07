# New Chat
## A script that allows you to have a spoken conversation with OpenAI's ChatGPT

### Install Dependencies
- Mac: `brew install portaudio flac`
- Ubuntu: `sudo apt install python3-pyaudio gnustep-gui-runtime`
- Both: `pip install pyaudio openai`
- Works on Mac and Ubuntu Linux

### Getting the API Key
- You need an OpenAI API key of your own for this program to work
- Start by going to https://openai.com/api/
- After setting up an account and generating an API key, add the API key to the `secret_key` variable in `keys.py` in the new-chat folder 


### How to Run
- Open terminal
- Navigate to the new-chat folder
- `python main.py`
- Speak your question or greeting into your microphone
- Wait for ChatGPT to respond
- Repeat
- Exit the program with `CTRL-C`

### Increase/Decrease Possible Response Length
- You may want to increase or decrease the max token length to avoid a high usage rate, or in order to increase the length of the possible response size
- Change `max_token_length` in `chat.py` to meet your needs

### To Do
- Make it work on Windows
- Make it easier to exit the program (not just `CTRL-C`)
