from django.http import HttpResponse
from django.shortcuts import render # HTMLファイルを返すのに必要なメソッド



def sign_up(request):
    if request.GET:
        msg = request.GET['msg']
        if msg=='hoge':
            return render(request, 'toketa/sign_up.html', {'msg': msg})
        else:
            return HttpResponse(f"{msg}")
    else:
        return HttpResponse("登録")

def sign_in(request):
    # if request.POST:
    #     name = request.POST['name']
    #     passwd = request.POST['paswadd']
    #     if name==user.name and passwd==user.passwd:
    #         render('home.html')
    #     else:
    #         render('sign_in.html')

    return HttpResponse("ログイン")

def sign_out(request):
    return HttpResponse("サインアウト")