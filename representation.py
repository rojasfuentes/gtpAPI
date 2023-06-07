from clean import frecuencia_clasificacion
import matplotlib.pyplot as plt

colores = ['red', 'green', 'black']

# Gráfico de barras de las frecuencias de clasificación con colores personalizados
frecuencia_clasificacion.plot(kind='bar', color=colores)
plt.xlabel('Clasificación')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de clasificaciones')
plt.show()

valores = frecuencia_clasificacion.values
etiquetas = frecuencia_clasificacion.index


# Crear el gráfico de pastel
plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%')

# Añadir título al gráfico
plt.title('Distribución de clasificaciones')

# Mostrar el gráfico de pastel
plt.show()