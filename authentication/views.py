from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse

# Create your views here.
class RegisterationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class UserNameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({
                'status': 1,
                'message': 'username should only contain alphanumeric character.',
                })
        return JsonResponse({
                'status': 0,
                'message': 'username valid.',
                })