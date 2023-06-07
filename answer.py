import pandas as pd


df = pd.read_csv(r'C:\Users\JFROJAS\Desktop\gtpAPI\Resultados.csv')
nombres_col = 'Palabra', 'Frecuencia'
df.columns = nombres_col
df_word_count = df[df['Frecuencia'] > 20] 
word_toerase = ['pandemia','refleja', 'malo', 'bueno','sentimientos', 'tweet' ,'negativos','malos','hacia','muestra','debido','personas','sugiere','habla','cómo','buenos','expresa','actual','puede','falta','forma','indica','hace','persona','sido','gran','muchas','pesar','medidas','además','aún'       ]
df_word_count = df_word_count[~df_word_count['Palabra'].isin(word_toerase)]

print(len(df_word_count))
print(df_word_count.head(50))


