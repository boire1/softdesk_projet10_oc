from django.shortcuts import render, redirect
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework import viewsets, permissions
from .forms import RegisterForm


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            if user.age < 15:
                # vous pouvez renvoyer une erreur ou rediriger l'utilisateur
                return render(request, 'user_app/error.html', {'message': 'Vous devez avoir plus de 15 ans pour vous inscrire.'})
            user.save()
            # log the user in and redirect them
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'user_app/register.html', {'form': form})

def profile(request):
    return render(request, 'user_app/profile.html')

from django.shortcuts import redirect

def some_view(request):
    # ... some code here
    return redirect('token_obtain_pair')
