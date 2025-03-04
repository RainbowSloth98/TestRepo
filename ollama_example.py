import ollama

prompt = "You are a Clony the clown, and will respond in funny jokes and puns."
context = "Who are you?"

modelfile='''
FROM llama2
PARAMETER num_ctx 4096
PARAMETER num_predict 4096
'''


ollama.create(model='clowner', modelfile=modelfile)


response = ollama.chat(
    model='clowner',
    messages=[
    {
        'role': 'system',
        'content': prompt,
    },

    {
      'role': 'user',
      'content': context,
    },],
    )

print(response['message']['content'])
