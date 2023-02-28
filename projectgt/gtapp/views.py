from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .models import Imagen, Person, Minigame
from .forms import RegistrationForm



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


class GameView(generic.ListView):
    model = Minigame
    template_name = 'games.html'
    context_object_name= 'ct_games'

    def palindromo(request):
        r"Palindrome function"
        if request.method == 'POST':
            palabra = request.POST.get('palabra', '')

            invertida = palabra[::-1]

            if invertida == palabra:
                return HttpResponse("Is Palindrome")
            else:
                return HttpResponse("Not is Palindrome")

        return render(request, 'games.html', palabra)

    def parorimpar(request):
        r"Odd or even function"

        if request.method == 'POST':
            num = request.POST.get('num', '')

            num = int(num)

            if num%2 == 0:
                return HttpResponse(num + "It's Even")
            else:
                return HttpResponse(num + "It's Odd") 
                
        return render(request, 'games.html', num)

    def get_queryset(self):
        return self.parorimpar, self.palindromo


class RegistrationView(generic.CreateView):
    model = User
    template_name = 'registration.html'
    context_object_name = 'context_registration'
    form_class = RegistrationForm

 
class ProfileView(generic.ListView):
    """View Profile User"""

    model = Person
    template_name = 'profile.html'
    

   

