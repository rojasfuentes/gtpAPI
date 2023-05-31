from toObject import all_filtered_data, all_filtered_data2
import openai

openai.api_key = "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"
filtered_tweets = all_filtered_data2[577:]

with open("respuestas.txt", "a",  encoding="utf-8") as file:
    for index, tweet in enumerate(filtered_tweets):
        print("Procesando tweet {} de {}".format(index + 1, len(filtered_tweets)))
        
        prompt = "Este tweet habla sobre la pandemia, puedes explicarme si refleja sentimientos buenos o malos?, por favor, LA PRIMERA PALABRA QUE ESCRIBAS SEA 'BUENO' O 'MALO' dependiendo del resultado, por favor dame también una breve explicación del porque después de eso: " + tweet

        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024
        )

        response = completion.choices[0].text.strip()

        file.write("Tweet: {}\n".format(tweet))
        file.write("Respuesta: {}\n\n".format(response))
