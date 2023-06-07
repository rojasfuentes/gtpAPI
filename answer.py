import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\GTP\auxiliar\Resultados.csv')
nombres_col = 'Palabra', 'Frecuencia'
df.columns = nombres_col
df_word_count = df[df['Frecuencia'] > 20] 
word_toerase = ['pandemia','refleja', 'malo', 'bueno','sentimientos', 'tweet' ,'negativos','malos','hacia','muestra','debido','personas','sugiere','habla','cómo','buenos','expresa','actual','puede','falta','forma','indica','hace','persona','sido','gran','muchas','pesar','medidas','además','aún','acerca','podría','haber','ser','parte','significa','mundo','señala','menciona','así','años','siendo','causa','relación','comparación','presenta','aquellos','implica','mostrando','largo','poder','cuanto','pueden','indignación','nivel','lidiar','revela','parece','nacional','negativas','países','año','pérdida','tratar','adelante','ayuda','seguir','prevenir','momento','idea','plena','genera','destaca','describe','alguien','frente','cosas','mal','tono','vez','relacionados','causado','india','millones','relacionada','acción','nuevas','medio','positiva','crítica','enfrentando','acelerar' ,'uso','lugar','refiere','tener','referencia','nueva','criticando','cantidad','manera','respecto','mayor','negativa','gestión','si','fin','esfuerzos','manejo','propagación','ahora','dos','unidos','mil','mejor','ayudar','frase','usuario','reflejando','tuit','todavía','mientras','representa','hacer','después','alto','demuestra','mismo','sugiriendo','sigue','méxico','dificultades','equipo','nuevo','decisión','trabajo','tratamientos','acciones','resultados','medios','respeto']
df_word_count = df_word_count[~df_word_count['Palabra'].isin(word_toerase)]

#df_word_count.to_excel(r'C:\Users\Mayo\OneDrive - Universidad Autónoma del Estado de México\Desktop\GTP\Resultados.xlsx', index = False)

df_word_count['Frecuencia'] = df_word_count['Frecuencia'] * 2.5
final = df_word_count['Frecuencia'].round(0)
df_word_count['Frecuencia'] = final


# Limitar el número de palabras a mostrar en el gráfico
num_palabras = 50
df_top_palabras = df_word_count.head(num_palabras)

# Crear el gráfico de barras horizontales
plt.figure(figsize=(10, 6))
plt.barh(df_top_palabras['Palabra'], df_top_palabras['Frecuencia'], color='green')
plt.xlabel('Frecuencia')
plt.ylabel('Palabra')
plt.title(f'Palabras más repetidas (Top {num_palabras})')
plt.tight_layout()

# Mostrar el gráfico
plt.show()