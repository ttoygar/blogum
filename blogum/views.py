from django.shortcuts import render, HttpResponse


def anasayfa(request):
    # return HttpResponse('Hello World!')
    return render(request, 'blogum/anasayfa.html')
