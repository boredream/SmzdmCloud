# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError
import leancloud
import os
import time
import json

engine = Engine()


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


@engine.define
def crawl(**params):
    # os.system('scrapy crawl smzdm')
    # time.sleep(5)
    fp = open('data.txt')
    for line in fp.readlines():
        data = json.loads(line)
        obj = leancloud.Object().create(class_name='Goods')
        obj.set('name', data['name'])
        obj.set('image', data['image'])
        obj.set('link', data['link'])
        obj.save()
        print data['name']


@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')


crawl()