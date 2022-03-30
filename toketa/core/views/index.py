from django.http import HttpResponse
from django.shortcuts import render # HTMLファイルを返すのに必要なメソッド

def home(request):
    return render(request, 'toketa/home.html')
    # return HttpResponse("うんこ")