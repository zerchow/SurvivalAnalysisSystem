# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext


def search_process_get(request):
    if 'search_content' in request.GET:
        message = 'get搜索的内容为：' + request.GET['search_content'].encode('utf-8')
    else:
        message = 'get空表单'
    print message
    return HttpResponse(content=message)


def search_process_post(request):
    print 'loading the post method'
    context = {}
    context.update(csrf(request=request))
    if 'search_content' in request.POST:
        message = 'post搜索的内容为：' + request.POST['search_content'].encode('utf-8')
    else:
        message = 'post空表单'
    print message
    return HttpResponse(content=message)


def search(request):
    print 'loading search page'
    return render_to_response(template_name='runoob_search.html', context=None, context_instance=RequestContext(request=request))


def get_post_model(request):
    path = request.path
    if request.method == 'GET':
        method = 'GET'
    elif request.method == 'POST':
        method = 'POST'
    get_dic = request.GET
    post_dic = request.POST
    content_length = request.META['CONTENT_LENGTH']
    content_type = request.META['CONTENT_TYPE']
    query_string = request.META['QUERY_STRING']  # 未解析的原始查询字符串
    remote_addr = request.META['REMOTE_ADDR']  # 客户端IP地址
    remote_host = request.META['REMOTE_HOST']  # 客户端主机名
    server_name = request.META['SERVER_NAME']  # 服务器主机名
    server_port = request.META['SERVER_PORT']  # 服务器端口
    http_accept_encoding = request.META['HTTP_ACCEPT_ENCODING']
    http_accept_language = request.META['HTTP_ACCEPT_LANGUAGE']
    http_host = request.META['HTTP_HOST']  # 客户发送的http主机头信息
    http_user_agent = request.META['HTTP_USER_AGENT']  # 客户端的user-agent字符串