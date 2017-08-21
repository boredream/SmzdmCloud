import leancloud


APP_ID = 'fMdvuP11j3fRLxco6VQ9Aj69-gzGzoHsz'
APP_KEY = 'VuP45bVSUIpo4fLGEmJgfuba'
MASTER_KEY = 'rOet8y51ojPaYTpNY3kX9ipk'
leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(True)

datas = leancloud.Query(query_class='Goods').find()
for data in datas:
    data.set('user', {
        '__type': 'Pointer',
        'className': '_User',
        'objectId': '5992a69f570c35006b7efa00'
    })
    data.save()
