from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
# Create your views here.

def baseview(request):
    return render(request,'LoginTest.html')

def trackph(request):
    return HttpResponse(request.META.get('HTTP_REFERER','/'))

def loginview(request):
    if request.user.is_authenticated:
        # return redirect(request.META.get('HTTP_REFERER','/'))
        return render(request,'LoginTest.html',locals())
    else:
        # return HttpResponse('error')
        if request.method == 'GET':
            request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
            # login_from
            return render(request,'LoginTest.html',locals())
        elif request.method == 'POST':
            username = request.POST.get("username",'')
            password = request.POST.get("password",'')
            if username != '' and password != '':
                user = authenticate(username=username, password=password)
                print(user)
                if user is not None:
                    login(request,user)
                    print('login Success')
                    return redirect(request.session['login_from'])
                    #
                else:
                    print(username,password,user)
                    # errormsg = '用户名或密码错误！'
                    return render(request,'LoginTest.html',locals())
            else:
                return JsonResponse({"e":"chucuo"})


def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'LoginTest.html')  
