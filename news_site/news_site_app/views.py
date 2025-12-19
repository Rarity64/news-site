from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def auth(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)    
    else:
        return render(request, 'auth.html')

def reg(request):
    return render(request, 'reg.html')
    



    



        # user = authenticate(request, email=email, password=password)
        # if user is not None:
        #     login(request, user)
        #     print(f'login: {username}, password: {password}')
        #     return JsonResponse({'status': 'success', 'message': 'OK'})
        # else:
        #     return JsonResponse({'status': 'error', 'message': 'Неверный логин и пароль'})