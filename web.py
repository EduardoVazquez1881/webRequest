from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

contenido = {
    '/': """
    <html lang="es">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Ana Lee </title>
        <link href="css/style.css" rel="stylesheet">
      </head>
      <body>
        <h1>Ana Lee </h1>
        <h2>Desarrolladora Web (Música/Diseño/Empresaria)</h2>
        <small>Este texto fue generado por Copilot:</small>
        <h3>
          ¡Hola! Soy Ana Lee, una desarrolladora web que se especializa en la creación
          de sitios web y aplicaciones web. Me encanta trabajar con tecnologías web modernas.
        </h3>
        <br />
        <h2>Proyectos</h2>
        <h3><a href="/proyecto/web-uno"> Web Estática - App de recomendación de libros </a></h3>
        <h3><a href="/proyecto/web-dos"> Web App - MeFalta, que película o serie me falta ver </a></h3>
        <h3><a href="/proyecto/web-tres"> Web App - Foto22, web para gestión de fotos </a></h3>
        <br />
      </body>
    </html>
    """,
    '/proyecto/web-uno': """
    <html>
      <h1>Proyecto: Web Estática - App de recomendación de libros</h1>
      <p>Este proyecto muestra una lista de libros recomendados basada en preferencias del usuario.</p>
    </html>
    """,
    '/proyecto/web-dos': """
    <html>
      <h1>Proyecto: MeFalta</h1>
      <p>Web App que te ayuda a recordar qué película o serie te falta ver.</p>
    </html>
    """,
    '/proyecto/web-tres': """
    <html>
      <h1>Proyecto: Foto22</h1>
      <p>Una web para gestionar y organizar tus fotos de manera eficiente.</p>
    </html>
    """
}


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
        # Obtener la ruta solicitada
        path = self.path
        
        # Buscar en el diccionario el contenido correspondiente a la ruta
        content = contenido.get(path, None)
        
        if content:
            # Si existe el contenido para esa ruta, devolverlo
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        else:
            # Si no existe, devolver un error 404
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>Página no encontrada</h1>".encode("utf-8"))

    ##def do_GET(self):
    ##    contenido = leer_archivo_html('home.html') #Estoy enviando el nombre del archivo como parametro al metodo creado
    ##    self.send_response(200)
    ##    self.send_header("Content-Type", "text/html")
    ##    self.end_headers()
    ##    self.wfile.write(contenido.encode("utf-8")) #Estoy ejectuando el servidor con la vista almacenada en contenido en lugar de get_response

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
