#! usr/bin/python3

# App que imprime "Adiós" en el navegador
import webappmulti

class appAdios():
	def parse(self, request, rest):
		return None
	
	def process(self, parsedResquest):
		return ("200 OK", "<html><body><h1>" + "¡Adiós!" + "</h1></body></html>")
