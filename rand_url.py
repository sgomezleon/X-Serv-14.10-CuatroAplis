#! usr/bin/python3

# App que devuelve una url aleatoria en el navegador
import webappmulti
import random


class randomURL():

	def parse(self, request, rest):
		return None

	def process(self, parsedRequest):

		url = random.randint(0,999999)
		answer = ("<html><body><h1><a href=http://localhost:1234/aleat/" + str(url) +">Dame otra</a>")
		return("200 OK", answer)
