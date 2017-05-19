import web
#coding=utf-8
urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class index:
    def GET(self):
        query = web.input()
        return query

class blog:
    def POST(self):
        data = web.input()
        return data
    def GET(self):
        return web.ctx.env
class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()