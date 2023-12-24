from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Profile,Post
from django.http import HttpResponse
# Create your views here.

def signup(request):
  try:
    if request.method == 'POST':
      fnm = request.POST.get('fnm')
      emailid = request.POST.get('emailid')
      pwd = request.POST.get('pwd')
      my_user = User.objects.create_user(fnm,emailid,pwd)
      my_user.save()
      user_model = User.objects.get(username = fnm)
      new_profile = Profile.objects.create(user = user_model,id_user=user_model.id)
      new_profile.save()
      if my_user is not None:
        login(request,my_user)
        return redirect('/')
      return redirect('/login')
  except:
    invalid = 'user already exists'
    return render (request,'signup.html',{'invalid':invalid})
  return render (request,'signup.html')
  

def login (request):
  if request.method == 'POST':
    fnm = request.POST.get('fnm')
    pwd = request.POST.get('pwd')
    print(fnm,pwd)
    userr = authenticate(request,username = fnm,password = pwd)
    if userr is not None:
      login(request,userr)
      return redirect('/')
    invalid = 'invalid credentials'
    return render(request,'loginn.html',{'invalid':invalid})
  return render(request,'loginn.html')

def logout(request):
  logout(request)
  return redirect ('login/')


def upload(request):
  if request.method == 'POST':
    user = request.user.username
    image = request.Files.get('image-upload')
    caption = request.POST['caption']
    new_post = Post.objects.create(user=user,image=image,caption=caption)
    new_post.save()
    return redirect('/')
  else:
    return redirect('/')
  
  

def home (request):
  return HttpResponse("Hello Django")


