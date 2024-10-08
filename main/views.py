from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request: object) -> object:
        context = {}
        return render(request, 'index.html', context)

    def post(self, request):
        return render(request, 'index.html', {'message': 'Data received'})


class SupportView(View):

    def get(self, request: object) -> object:
        context = {}
        return render(request, 'support.html', context)

    def post(self, request):
        return render(request, 'support.html', {'message': 'Data received'})
