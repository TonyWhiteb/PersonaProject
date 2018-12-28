from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def baseview(request):
    return render(request,'LoginPage.html')

def trackph(request):
    return HttpResponse(request.META.get('HTTP_REFERER','/'))

def loginview(request):
    if request.user.is_authenticated:
        # return redirect(request.META.get('HTTP_REFERER','/'))
        return render(request,'LoginPage.html',locals())
    else:
        # return HttpResponse('error')
        if request.method == 'GET':
            # request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
            # login_from
            return render(request,'LoginPage.html',locals())
        elif request.method == 'POST':
            username = request.POST.get("username",'')
            password = request.POST.get("password",'')
            if username != '' and password != '':
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login(request,user)
                    print('login Success')
                    # return redirect(request.session['login_from'])
                    return render(request,'LoginPage.html',locals())
                    #
                else:
                    # print(username,password,user)
                    errormsg = 'Incorrect Email or Password!'
                    return render(request,'LoginPage.html',locals())
            else:
                return JsonResponse({"e":"chucuo"})


def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'LoginPage.html')

    # return HttpResponse('hello')
@login_required
def ScannerPop(request):
    pass
