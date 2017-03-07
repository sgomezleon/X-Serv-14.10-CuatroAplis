#! usr/bin/python3

# App que devuelve una suma en el navegador
import webappmulti

class appSuma():

	primer_sumando = True

	def parse(self, request, rest):
		
		try:
			rest = int(rest[1:])	
			return rest
		except ValueError:
			return None
		
	def process(self, parsedRequest):
		try:
			if parsedRequest == 'favicon.ico':
				return None
			elif primer_sumando:
				sumando1 = sumando
				return ("200 OK", "<html><body><h1>Primer sumando: " + sumando1 + "</h1></body></html>")
			else:
				suma = sumando1 + sumando
				return ("200 OK", "<html><body><h1>Resultado: " + suma + "</h1></body></html>")
		except:
			return None
