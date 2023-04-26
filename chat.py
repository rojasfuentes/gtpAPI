import openai

openai.api_key = "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"

completion = openai.Completion.create(engine= "text-davinci-003",
                                      prompt='Qué es ChatGTP?',
                                      max_tokens= 2048)

print(completion.choices[0].text)