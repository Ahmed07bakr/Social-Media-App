from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Profile,Post,LikePost
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
    image = request.FILES.get('image-upload')
    caption = request.POST['caption']
    new_post = Post.objects.create(user=user,image=image,caption=caption)
    new_post.save()
    return redirect('/')
  else:
    return redirect('/')
  
  

def home (request):
  post = Post.objects.all().order_by('-created_at')
  # profile = Profile.objects.get(user = request.user)
  context = {
    'post':post,
    # 'profile':profile,
  }
  return render (request,'main.html',context)



def likes(request,id):
  if request.method == 'GET':
    username=request.user.username
    post = get_object_or_404(Post,id=id)
    like_filter = LikePost.objects.filter(post_id=id,username=username).first()
    if like_filter is None:
      new_like = LikePost.objects.create(post_id=id,username=username)
      post.no_of_likes += 1
      
    else:
      like_filter.delete()
      post.no_of_likes -=  1
      
  post.save()
  return redirect('/')


def home_posts(request,id):
  post = Post.objects.get(id=id)
  profile = Profile.objects.get(user=request.user)
  context = {
    'profile':profile,
    'post':post,
  }

  return render (request,'main.html',context)


def explore (request):
  post = Post.objects.all().order_by('created_at')
  # profile = Profile.objects.get(user=request.user)
  context={
    'post':post,
    # 'profile':profile,

  }
  return render(request,'explore.html',context)


def profile(request,id_user):
  user_object = User.objects.get(username=id_user)
  profile = Profile.objects.get(user=request.user)
  user_profile = Profile.objects.get(user=user_object)
  user_posts = Post.objects.filter(user=id_user).order_by('created_at')
  user_post_length = len(user_posts)
  context={
    'user_object':user_object,
    'profile':profile,
    'user_profile':user_profile,
    'user_posts':user_posts,
    'user_post_length':user_post_length,
  }
  return render(request,'profile.html',context)






