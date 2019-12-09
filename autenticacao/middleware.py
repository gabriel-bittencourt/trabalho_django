from django.http import HttpResponseRedirect
from trabalho import settings
import time

class LoginRequiredMiddleware:
   def __init__(self, get_response):
      self.get_response = get_response
      self.login_path = getattr(settings, 'LOGIN_URL')

   def __call__(self, request):

      print("\n-----------------------------------------------------")
      print("--------- Início do LoginRequiredMiddleware ---------")
      print("-----------------------------------------------------")

      # print("************* Request GET Parameters *************")
      for chave, valor in request.GET.items():
         print(f'\nGET <==> request.path = {request.path} - Chave: {chave} <==> Valor: {valor}')

      # print("************* Request POST Parameters ************")
      for chave, valor in request.POST.items():
         print(f'\nPOST <==> request.path = {request.path} - Chave: {chave} <==> Valor: {valor}')

      # print("********************* Cookies ********************")
      for chave, valor in request.COOKIES.items():
         print(f'\nANTES - COOKIE <==> request.path = {request.path} - Chave: {chave} <==> Valor: {valor}')
      
      request.inicio = int(round(time.time() * 1000)) # Isso é um atributo!

      response = self.get_response(request)

      request.fim = int(round(time.time() * 1000))

      diferenca = request.fim - request.inicio

      print (f'\ndiferenca = {diferenca}')

      # Code to be executed for each request/response after
      # the view is called.

      for chave, valor in request.COOKIES.items():
         print(f'\nDEPOIS - COOKIE <==> request.path = {request.path} - Chave: {chave} <==> Valor: {valor}')

      print(f'\nDEPOIS - RESPONSE <==> response.cookies = {response.cookies}')

      for chave, valor in request.session.items():
         print(f'\nDEPOIS - SESSION <==> request.session.session_key = {request.session.session_key} - Chave: {chave} <==> Valor: {valor}')

      print("\n-----------------------------------------------------")
      print("---------- Logo antes de retornar response ----------")
      print("-----------------------------------------------------")

      return response
   
   # class A:
   #    def __init__(self):
   #       print('init')
   #    def __call__(self):
   #       print('call')
   #
   # a = A() ==> provoca a execução do método init
   # a()     ==> provoca a execução do método call (o objeto é chamado como uma função)
   #    