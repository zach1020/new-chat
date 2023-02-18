import os
import openai

import keys

def chat(my_prompt):
	#openai.organization = 
	openai.api_key = keys.secret_key

	max_token_length = 500

	completion_object = openai.Completion.create(
		model = "text-davinci-003",
		prompt= my_prompt,
		max_tokens = max_token_length,
		temperature = 0
	)

	response = completion_object['choices'][0]['text'].strip()

	print(response)
	return response