from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MyUser
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
            # request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
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
                    # return redirect(request.session['login_from'])
                    return render(request,'LoginTest.html',locals())
                    #
                else:
                    # print(username,password,user)
                    errormsg = 'Incorrect Email or Password!'
                    return render(request,'LoginTest.html',locals())
            else:
                return JsonResponse({"e":"chucuo"})


def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'LoginTest.html')

    # return HttpResponse('hello')


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_validate': MyUser.objects.filter(username__iexact = username).exists()
    }
    if data['is_validate'] :
        data['success_msg'] = 'Login Success!'
    else:
        data['error_msg'] = 'Invalidate Username!'
    return JsonResponse(data)

def test(request):
    if request.user.is_authenticated:
        logout(request)
        # return redirect(request.META.get('HTTP_REFERER','/'))
        return render(request,'testpage.html')
    else:
        # return HttpResponse('error')
        if request.method == 'GET':
            # request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
            # login_from
            return render(request,'testpage.html',locals())
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
                    return render(request,'testpage.html',locals())
                    #
                else:
                    # print(username,password,user)
                    errormsg = 'Incorrect Email or Password!'
                    return render(request,'testpage.html',locals())
            else:
                return JsonResponse({"e":"chucuo"})
def testlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'testpage.html')

@login_required
def ScannerPop(request):
    pass


