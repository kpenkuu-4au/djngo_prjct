from django.shortcuts import render


def func_tmpl(request):
    return render(request, 'second_task/func_template.html')
