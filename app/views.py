from django.shortcuts import render
from .models import FAQ,Course
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User


def index(request):
    faqs = FAQ.objects.all()

    ux_ui_courses = Course.objects.filter(title='UX/UI Design')
    python_courses = Course.objects.filter(title='Python')
    js_courses = Course.objects.filter(title='JavaScript')
    pm_courses = Course.objects.filter(title='PM')
    html_css_courses = Course.objects.filter(title='HTML/CSS')

    context = {
        'faqs': faqs,
        'ux_ui_courses': ux_ui_courses,
        'python_courses': python_courses,
        'js_courses': js_courses,
        'pm_courses': pm_courses,
        'html_css_courses': html_css_courses,
    }

    return render(request, 'app/index.html', context)


def regV(request):
    form = UserCreationForm
    context = {'form':form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            redirect('home')
    return render(request,'app/register.html',context)


def loginVi(request):
    if request.method =='POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=name)
        except Exception as e:
            print(f"no user {e}")
            user = authenticate(username=name, password=password)
            login(request,user)
            redirect('home')
    return render(request,'app/login.html')


