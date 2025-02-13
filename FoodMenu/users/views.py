from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        # Redirect logged-in user to the profile page
        return redirect('profile')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account has been created :)')
            form.save()
            return redirect(reverse('login'))
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {
        'form':form,
    })

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')




class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect logged-in user to the profile page
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)