from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import CustomUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    else:
        form = CustomUserForm()

        if request.method == "POST":
            form = CustomUserForm(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get("username")

                messages.success(
                request, "Account has been successfully created for " + user)
                return redirect('login')

        context = {
            'form': form
        }

        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('tasks')
            else:
                messages.info(request, "Invalid username or password")

        return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)

    return render(request, 'accounts/logout.html')
