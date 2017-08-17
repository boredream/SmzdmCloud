# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError
from leancloud import LeanCloudError
import leancloud
import os
import time
import json

engine = Engine()


@engine.define
def crawl(**params):
    print 'start crawl'
    os.system('scrapy crawl smzdm --nolog')
    time.sleep(5)

    print 'start save crawl data'
    fp = open('data.txt')
    for line in fp.readlines():
        data = json.loads(line)

        try:
            exist_data = leancloud.Query(query_class='Goods')\
                .equal_to('name', data['name']).first()
        except LeanCloudError:
            exist_data = None

        if exist_data:
            # 已经存在数据，只更新点赞信息
            exist_data.set('worth', data['worth'])
            exist_data.save()
            continue

        obj = leancloud.Object().create(class_name='Goods')
        obj.set('name', data['name'])
        obj.set('image', data['image'])
        obj.set('link', data['link'])
        obj.set('worth', data['worth'])
        obj.save()
    print 'crawl done!'


@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')
