from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.models import User
from .models import Imagen, Person
from .forms import RegistrationForm
from PyQt5.QtWidgets import QMessageBox
import datetime
from django.contrib import messages



class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Imagen

    def get_queryset(self):
        return Imagen.objects.all()

class ImagenView(generic.ListView):
    model = Imagen
    template_name = 'imagen.html'
    context_object_name= 'context_imagen'

    def get_queryset(self):
        return Imagen.objects.all()
        
class RegistrationView(generic.CreateView):
    model = User
    template_name = 'registration.html'
    context_object_name = 'context_registration'
    form_class = RegistrationForm

class ProfileView(generic.ListView):
    """View Profile User"""

    model = Person
    template_name = 'profile.html'
    
class PalindromoAlsoOddorEvenView(View):
        r"Palindrome and Odd or Even class"

        template_name = 'dinamics.html'

        def check_palindromo(self, word):

            cleaned_palabra = word.lower().replace(' ', '')

            """       palindromo = cleaned_palabra == cleaned_palabra[::-1]

            if palindromo:
                return messages.success(self.request, 'Es un Palidromo')
            else:
                return messages.error(self.request, 'No es un Palidromo') """
        
            return cleaned_palabra == cleaned_palabra[::-1]
        
        def check_oddoreven(self, num):
          
            num = int(num)

            return num%2 == 0

        def get(self, request):
            return render(request, self.template_name)
        
        def post(self, request):

            word = request.POST.get('word')
            num = request.POST.get('num')

            palindromo = self.check_palindromo(word)
            odd_even = self.check_oddoreven(num)
            
            context = {'word': word, 
                       'num': num, 
                       'palindromo': palindromo, 
                       'odd_even': odd_even}

            return render(request, self.template_name, context)

       
