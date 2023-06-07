import pandas as pd

data = []
with open(r'C:\Users\JFROJAS\Desktop\gtpAPI\respuestas.txt', 'r',encoding="utf-8") as file:
    lines = file.readlines()
    tweet = ''
    respuesta = ''
    for line in lines:
        if line.startswith('Tweet:'):
            if tweet != '':
                data.append({'Tweet': tweet, 'Respuesta': respuesta})
            tweet = line.replace('Tweet:', '').strip()
        elif line.startswith('Respuesta:'):
            respuesta = line.replace('Respuesta:', '').strip()
    # Añadir el último tweet y respuesta al final del bucle
    data.append({'Tweet': tweet, 'Respuesta': respuesta})

df = pd.DataFrame(data)

df['Clasificación'] = df['Respuesta'].apply(lambda x: 'Bueno' if 'bueno' in x.lower() else 'Malo' if 'malo' in x.lower() else 'Otro')


#print(df['Clasificación'].value_counts())

#df_otro =df.loc[df['Clasificación'] == 'Otro']
#print(df.head(50))

#df.to_cs(r'C:\Users\JFROJAS\Desktop\gtpAPI\respuestas.csv', index=False)

frecuencia_clasificacion = df['Clasificación'].value_counts()
