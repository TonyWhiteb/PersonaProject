from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
# Create your views here.

def baseview(request):
    return render(request,'LoginTest.html')

def trackph(request):
    return HttpResponse(request.META.get('HTTP_REFERER','/'))

def loginview(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER','/'))
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
                    return redirect('',user = request.user)
                else:
                    print(username,password,user)
                    # errormsg = '用户名或密码错误！'
                    return render(request,'LoginTest.html',locals())
            else:
                return JsonResponse({"e":"chucuo"})
#     if request.user.is_authenticated == True:
# # "Using User.is_authenticated() and User.is_anonymous() as methods rather than properties is no longer supported."
#         # return render(request,'LoginTest.html')
#         return redirect(request.META.get('HTTP_REFERER','/'))
#     elif request.method == 'POST':
#         username = request.POST.get("username","")
#         password = request.POST.get("password","")
#         if username != '' and password != '':
#                 user = authenticate(username=username, password=password)
#                 print(user)
#                 if user is not None:
#                     login(request,user)
#                     print("Login Success!")
#                     return redirect(request.META.get('HTTP_REFERER','/'))
#                 else:
#                     print(username,password,user)
#                     # errormsg = 'Something Wrong!'
#                     return redirect(request.META.get('HTTP_REFERER','/'))
#         else:            
#                 return JsonResponse({"e":"chucuo"})
    # return render(request,'LoginTest.html',locals())
    # return HttpResponse(request.user.is_authenticated)

