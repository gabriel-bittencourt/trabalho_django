from django.http import HttpResponseRedirect
from trabalho import settings
import time

class LoginRequiredMiddleware:
   def __init__(self, get_response):
      self.get_response = get_response
      self.login_path = getattr(settings, 'LOGIN_URL')

   def __call__(self, request):

      request.inicio = int(round(time.time() * 1000)) 

      response = self.get_response(request)

      request.fim = int(round(time.time() * 1000))

      diferenca = request.fim - request.inicio

      return response
   
