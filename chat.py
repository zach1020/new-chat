import openai
import stt
import tts

import keys

def chat(conversation):
    """
    Use ChatGPT
    """
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=conversation
    )
    #print(completion)
    response = {"role": "system", "content": completion["choices"][0]["message"]["content"].strip()}
    tts.speak(response["content"])
    print(response["content"])

    return response


def prompt(): 
    """
    Get the prompt from user
    """
    prompt = {"role": "user", "content": stt.stt()}
    return prompt

def add_to_conversation(conversation, to_add):
    """
    Add something to the overall conversation
    """
    conversation.append(to_add)

def converse(conversation):
    """
    1. Get prompt from user
    2. Add prompt to conversation
    3. Get ChatGPT response
    4. Add response to conversation
    """
    add_to_conversation(conversation, prompt())
    add_to_conversation(conversation, chat(conversation))
