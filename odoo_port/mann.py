# -*- coding:utf-8 -*-
import sys
from serviceAPI import WebAPI
reload(sys)
sys.setdefaultencoding('UTF-8')
class login():
    def __init__(self,url=None, db=None, username=None, password=None):
        '''
        self.wapi = WebAPI(url='http://erp.mei1.info')
        self.wapi.login(db='odoo_171024',username='admin',password='meiwen666666')
        self.wapi = WebAPI(url='http://erp.temp.mei1.info')
        print self.wapi.login(db='odoo_171024',username='admin',password='meiwen666666')
        '''
        self.wapi = WebAPI(url=url)
        self.wapi.login(db=db, username=username,password=password)
        
    def get_wapi(self):
        return self.wapi



class mantance_status:
    def __init__(self, wapi):
        self.wapi = wapi

    def read(self):
        record_ids = self.wapi.search_read('res.partner',domain=[('x_maintance_record_id','!=',False)],fields={'fields':['x_maintance_record_id']})
        for parts in record_ids:
            m_id = parts['x_maintance_record_id'][0] 
            
            manta_re = self.wapi.search_read('x_maintance_record',domain=[('id','=',m_id)],fields={'fields':['maint_status']})
            if manta_re[0]['maint_status']:
                p_id = parts['id']
                status = manta_re[0]['maint_status']
                self.wapi.update('res.partner',p_id ,{'maint_status':status})
                print p_id, status

if __name__ == '__main__':
    #生产
    log = login(url='https://erp303.mei1.com',db='odoo_new',username='admin', password='meiwen666666')
    #测试
    #log = login(url='http://erp.dev.mei1.info',db='odoo_dev',username='admin', password='meiwen666666')
    #正式开始导入程序
    wapi = log.get_wapi()
    mantance_status(wapi).read()
    


