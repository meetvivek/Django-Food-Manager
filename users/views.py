from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = user.profile
            profile.full_name = form.cleaned_data.get('full_name')
            profile.city = form.cleaned_data.get('city')
            profile.state = form.cleaned_data.get('state')
            profile.pin_code = form.cleaned_data.get('pin_code')
            profile.favorite_food = form.cleaned_data.get('favorite_food')

            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()
            
            username = (form.cleaned_data.get('username')).upper()
            messages.success(request, f'Welcome "{username}", your account is created Successfully.🥳')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')
