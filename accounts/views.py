from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# def registerPage(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account was created for {}'.format(form.cleaned_data.get('email')))
#             return redirect('login')
#
#
#
#     context = {'form': form}
#     return render(request, 'accounts/register.html', context)
#
def loginPage(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if not user.is_superuser:
                messages.error(request, 'You are not admin, Sorry =(')
                return redirect('logout')
            else:
                messages.success(request, 'Login success!')
                return redirect('dashboard')
        else:
            messages.info(request, 'Почта или пароль не правильны!')
            return render(request, 'accounts/login.html', context)

    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return  redirect('login')