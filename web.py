from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

def leer_archivo_html(nombre_archivo): #Estoy creado este metodo para leer un archivo el cual asignara el parametro
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return "<h1>Error 404: Archivo no encontrado</h1>"


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        contenido = leer_archivo_html('home.html') #Estoy enviando el nombre del archivo como parametro al metodo creado
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(contenido.encode("utf-8")) #Estoy ejectuando el servidor con la vista almacenada en contenido en lugar de get_response

    def get_response(self):
        return f"""
    <h1> Hola Web </h1>
    <h1>{self.url().path.split('/')[-2]}: {self.url().path.split('/')[-1]} {self.query_data()} <h1>
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
