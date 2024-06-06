from django.shortcuts import render
from .models import FAQ,Course


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
