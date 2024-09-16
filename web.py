from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

# Definición del contenido para diferentes rutas en el diccionario 'contenido'
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
# Función para leer archivos HTML desde el sistema de archivos
def leer_archivo_html(nombre_archivo): 
    # Esta función intenta leer un archivo HTML del sistema de archivos. Si el archivo no existe, devuelve un mensaje de error 404.
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        return "<h1>Error 404: Archivo no encontrado</h1>"

# Clase que maneja las solicitudes HTTP GET
class WebRequestHandler(BaseHTTPRequestHandler):
    
    # Método para analizar la URL de la solicitud y obtener sus componentes
    def url(self):
        return urlparse(self.path)

    # Método para convertir la cadena de consulta en un diccionario clave-valor
    def query_data(self):
        return dict(parse_qsl(self.url().query))
    
    # Método para manejar solicitudes GET
    def do_GET(self):
        # Obtener la ruta solicitada
        path = self.path
        
        # Buscar en el diccionario el contenido correspondiente a la ruta
        content = contenido.get(path, None)
        
        if content:
            # Si existe contenido para la ruta solicitada:
            self.send_response(200)  # Envía un código de respuesta HTTP 200 (OK)
            self.send_header("Content-Type", "text/html")  # Añade una cabecera que indica que el contenido es HTML
            self.end_headers()  # Finaliza el envío de cabeceras
            self.wfile.write(content.encode("utf-8"))  # Escribe y envía el contenido HTML codificado en UTF-8
        else:
            # Si no existe contenido para la ruta solicitada:
            self.send_response(404)  # Envía un código de respuesta HTTP 404 (Página no encontrada)
            self.send_header("Content-Type", "text/html")  # Añade una cabecera indicando que el contenido devuelto es HTML
            self.end_headers()  # Finaliza el envío de cabeceras
            self.wfile.write("<h1>Página no encontrada</h1>".encode("utf-8"))  # Escribe y envía un mensaje de error en HTML

    # Método adicional que no se utiliza actualmente, pero devuelve detalles de la solicitud
    def get_response(self):
        return f"""
    <h1> Hola Web </h1>
    <h1>{self.url().path.split('/')[-2]}: {self.url().path.split('/')[-1]} {self.query_data()} <h1>
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""

# Inicialización del servidor
if __name__ == "__main__":
    print("Starting server")
    print("prueba")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)  # Inicia el servidor en localhost en el puerto 8000
    server.serve_forever()  # Mantiene el servidor en ejecución de forma indefinida
