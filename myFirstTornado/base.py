from tornado import web, ioloop, httpserver

#业务处理模块 部门
class MainPageHandler(web.RequestHandler):
    def get(self, *arg, **kwargs):
       # self.write('the first project of my own')
        self.render('index.html')

#业务处理模块 部门
class CreateHandler(web.RequestHandler):
    def get(self, *arg, **kwargs):
        #self.write('the first project of my own')
        self.render('create.html')

# 路由 分机号
application = web.Application([
    (r"/create", CreateHandler),
    (r"/", MainPageHandler)
])

#socket 服务器 前台
if __name__ == '__main__':

    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
