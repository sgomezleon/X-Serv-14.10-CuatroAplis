#! usr/bin/python3

# App que imprime Hola en el navegador
import webappmulti

class appHola():
	def parse(self, request, rest):
		return None
	
	
	def process(self, parsedResquest):
		return ("200 OK", "<html><body><h1>" + "¡Hola!" + "</h1></body></html>")
