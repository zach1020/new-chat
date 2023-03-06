import openai
import chat
import keys


# Main

openai.api_key = keys.secret_key

master_conversation = []


while True:
    print("Press CTRL-C to Quit")
    chat.converse(master_conversation)
