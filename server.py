from urllib import parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import usuarios
import comentarios

import math

usuarios = usuarios.usuarios()
comentarios = comentarios.comentarios()

#Duma Roberto Zelaya Mejia 
#Roberto Carlos Hernandez Melendez
#Jose Roberto Del Rio Maravilla

class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
         if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        
         elif self.path == '/consultar-usuario':
            resp = usuarios.consultar_usuarios()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

         elif self.path == '/consultar-comentarios':
            resp = comentarios.consultar_comentario()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))
        
        
         else:
            return SimpleHTTPRequestHandler.do_GET(self)
            
    def do_POST(self):
        print("Peticion recibida")

        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        data = data.decode('utf-8')
        data = parse.unquote(data)
        data = json.loads(data)
        if self.path == '/usuario':
            resp = usuarios.administrar_usuarios(data)
        elif self.path == '/comentarios':
            resp = comentarios.administrar_comentario(data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(dict(resp=resp)).encode('utf-8'))

    
#Iniciar el servidor en el puerto 3001 
print("Iniciando el servidor en el puerto 3001")
server = HTTPServer(('localhost', 3001), servidorBasico)
server.serve_forever()