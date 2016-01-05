from django.http import HttpResponse
from django.shortcuts import render
import os


def hello(request):
    # return HttpResponse(content='Hello World')
    context = {}
    context['runoob_hello'] = 'Hello Template'
    context['runoob_list'] = [1, 2, 3, 4]
    return render(request=request, template_name='runoob_hello.html', context=context)


def get_image(request):
    dirname = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')
    print dirname
    image_data = open(dirname + '/images/lena.jpg', 'rb').read()
    return HttpResponse(image_data)
