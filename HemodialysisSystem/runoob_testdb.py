# -*- coding: utf-8 -*-

from django.http import HttpResponse
from main_analysis_app.models import RunoobTest


def testdb(request):
    # insert
    # test = RunoobTest(name='jiuyihu')
    # test.save(force_insert=False, force_update=False, using=None, update_fields=None)
    # return HttpResponse(content='<p>数据添加成功</p>')

    # select
    response = ''
    response1 = ''
    list = RunoobTest.objects.all()  # select * from table
    response2 = RunoobTest.objects.filter(id=1)  # select * from table where something
    response3 = RunoobTest.objects.get(id=1)  # just find one
    response4 = RunoobTest.objects.order_by('name')[0: 2]  # offset 0 limit 2
    response5 = RunoobTest.objects.order_by('id')  # sort by id
    response6 = RunoobTest.objects.filter(name='jiuyihu').order_by('id')  # link the operations
    for var in list:
        response1 += str(var.id) + ',' + var.name + ' == '
    response = response1
    return HttpResponse(content='<p>' + response + '</p>')

    # update
    # test = RunoobTest.objects.get(id=1)
    # test.name = 'jiuyihu_modify'
    # test.save()
    # # or
    # RunoobTest.objects.filter(id=1).update(name='jiuyihu_modify')
    # # all
    # RunoobTest.objects.all().update(name='jiuyihu_modify')
    # return HttpResponse(content='<p>修改成功</p>')

    # delete
    # test = RunoobTest.objects.get(id=1)
    # test.delete(using=None, keep_parents=False)
    # # or
    # RunoobTest.objects.filter(id=1).delete()
    # # all
    # RunoobTest.objects.all().delete()
    # return HttpResponse(content='<p>删除成功</>')
