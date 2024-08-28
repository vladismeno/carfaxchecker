from django.shortcuts import render
from django.views import View


class LoginView(View):

    def get(self, request: object) -> object:
        context = {}
        return render(request, 'users/login.html', context)

    def post(self, request):
        return render(request, '/users/login.html', {'message': 'Data received'})


class RegisterView(View):

    def get(self, request: object) -> object:
        context = {}
        return render(request, 'users/register.html', context)

    def post(self, request):
        return render(request, '/users/register.html', {'message': 'Data received'})
