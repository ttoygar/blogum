from django.shortcuts import render, HttpResponse


def anasayfa(request):
    # return HttpResponse('Hello World!')
    return render(request, 'blogum/anasayfa.html')


def halk_ekmek(request):
    return  render(request, 'blogum/halk_ekmek.html')
