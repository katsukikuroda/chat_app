from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
from .forms import LoginForm, SignUpForm
from .models import User
from django.contrib.auth.decorators import login_required 

def index(request):
    return render(request, 'main/index.html')

def signup(request):
    # ↓26で変更
    if request.method == "GET":
        form = SignUpForm()

    elif request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)

            return redirect("index")

    context = {"form": form}
    return render(request, "main/signup.html", context)

#↓27 login関数をLoginViewクラスに差替
class LoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = "main/login.html"

#↓27で追加 28で変更
@login_required
def friends(request):
    friends = User.objects.exclude(id=request.user.id)
    # friends = User.objects.all()
    context = {"friends": friends}
    return render(request, "main/friends.html", context)

#↓28で追加
@login_required
def settings(request):
    return render(request, "main/settings.html")
