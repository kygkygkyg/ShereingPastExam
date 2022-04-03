from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required



from .. import models

# from core.models import 


def example_crud(request):
    if request.POST:
        # >>>>>>>>>> userのcreate
        name = request.POST["name"]
        email = request.POST["email"]
        passwd = request.POST["passwd"]
        print('NOW:', name, email, passwd)
        try:
            user = models.User.objects.create_user(
                username=name,
                email=email,
            )
        except Exception as e:
            print(e)
            return redirect('example')
        auth_login(request, user)
        print('SUCCESS')
        print(models.User.objects.all())
        # example_login(request)
        # <<<<<<<<<<<


        # >>>>>>>>>>> Post, Bookのテスト
        

        if name=='':
            return render(request, 'example/example.html')
        if email=='':
            return render(request, 'example/example.html')
        if passwd=='':
            return render(request, 'example/example.html')
        
        
    return render(request, 'example/example.html')


@login_required()
def example_login(request):
    print('LOGIN OK')
    return redirect('example')