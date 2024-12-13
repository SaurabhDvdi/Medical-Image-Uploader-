from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        files = request.FILES.getlist('photo')

        if form.is_valid():
            for file in files:
                image_instance = Image(photo=file)
                image_instance.save()
            return redirect('home')
    else:
        form = ImageForm()

    img = Image.objects.all()        
    # form = ImageForm()
    return render(request,'imageapp\home.html',{'form':form,'img':img})

def sign_in(request):
    if request.method == 'POST':
        # Handle login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to your desired page after login
        else:
            messages.error(request, "Invalid username or password.")
    
    # Handle registration
    if request.method == 'POST' and 'register' in request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('sign_in')  # Redirect to sign-in page
    else:
        form = UserCreationForm()
    
    return render(request, 'imageapp/sign_in.html', {'form': form})