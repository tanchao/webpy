import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        name = 'bob'
        return render.index(name)

if __name__ == '__main__':
    app.run()
