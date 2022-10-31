from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
from .models import User


@permission_required('users.is_admin')
def admin(request):
    inactive_users = User.objects.exclude(is_active=True)
    return render(request, 'users/admin_page.html', {'inactive_users': inactive_users})


def register(request):
    user = request.user
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            subject = 'Registration Confirmation'
            message = f'Hi {username}, thank you for registering. An Admin has to approve your status as a department ' \
                      f'employee. \n' \
                      f'You will be noticed as soon as your status changes.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, f'Account created for {username}! Validation pending')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
