import cloud
import leancloud


APP_ID = "fMdvuP11j3fRLxco6VQ9Aj69-gzGzoHsz"
APP_KEY = "VuP45bVSUIpo4fLGEmJgfuba"
MASTER_KEY = "rOet8y51ojPaYTpNY3kX9ipk"
leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
leancloud.use_master_key(True)

cloud.crawl()
