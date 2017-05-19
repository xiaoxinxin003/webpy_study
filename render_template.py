#coding=utf-8
import web
import MySQLdb
import MySQLdb.cursors
import template

render = web.template.render('templates')
urls = (
    # 匹配范围更大的放后面。
    '/index', 'index',
    '/article','article',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

# 请求参数获取web.input()
class index:
    def GET(self):
        query = web.input()
        # 跳转
        return web.seeother('/article')

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
class article:
    def GET(self):
        conn = MySQLdb.connect(host='localhost', user='root', passwd='focus', db='world', port=3306)
        cur = conn.cursor()
        cur.execute('select  Name from city limit 0,50')
        r = cur.fetchall()
        cur.close()
        conn.close()
        print r

        return render.city(r)

# class hello:
#     def GET(self, name):
#         if not name:
#             name = 'World'
#         return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()