from urllib import parse
from http.server import HTTPServer, BaseHTTPRequestHandler

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import math

#Duma Roberto Zelaya Mejia 
#Roberto Carlos Hernandez Melendez
#Jose Roberto Del Rio Maravilla

#obtencion de los datoas de entrenamiento
temperaturas = pd.read_csv("dataset.csv", sep=";")
sns.scatterplot(temperaturas["Celcius"], temperaturas["Fahrenheits"])

#datos de entrada y salida
celsius = temperaturas["Celcius"]
fahrenheit = temperaturas['Fahrenheits']

#modelo de entrenamiento
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

#compilar el modelo
modelo.compile(optimizer=tf.keras.optimizers.Adam(1),loss='mean_squared_error')

#entrenamiento del modelo
epocas = modelo.fit(celsius, fahrenheit, epochs=100)

#Clase para definir el servidor http. Solo recibe solicitudes POST.
class servidorBasico(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Peticion GET recibida")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Server initialiced in 3001 port'.encode())

    def do_POST(self):
        print("Peticion recibida")

        #Obtener datos de la peticion y limpiar los datos
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode()
        data = parse.unquote(data)
        data = float(data)

        #Realizar y obtener la prediccion
        prediction_values = modelo.predict([data])
        print('Prediccion final: ', prediction_values)
        prediction_values = str(prediction_values[0][0])

        #Regresar respuesta a la peticion HTTP
        self.send_response(200)
        #Evitar problemas con CORS
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(prediction_values.encode())

#Iniciar el servidor en el puerto 3001 
print("Iniciando el servidor... en el puerto 3001")
server = HTTPServer(('localhost', 3001), servidorBasico)
server.serve_forever()