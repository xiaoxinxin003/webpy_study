#coding=utf-8
import web
import template

render = web.template.render('templates')
urls = (
    # 匹配范围更大的放后面。
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

# 请求参数获取web.input()
class index:
    def GET(self):
        query = web.input()
        return query

# 请求参数获取web.input()   请求头获取：web.ctx.env
class blog:
    def POST(self):
        data = web.input()
        return data
    def GET(self):
        return web.ctx.env
class hello:
    def GET(self, name):
        return render.template01(name)

# class hello:
#     def GET(self, name):
#         if not name:
#             name = 'World'
#         return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()