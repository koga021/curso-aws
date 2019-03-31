
import jinja2
import os
import sys
import requests
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Oi Cheguei no Tornado BE")

class CadastrarMateria(tornado.web.RequestHandler):
    def post(self):
        
        #self.write("Hello, world")
        operacao = self.get_argument('operacao')
        categoria = self.get_argument('categoria')
        titulo = self.get_argument('titulo')
        corpo = self.get_argument('corpo')
        self.write("Categoria " + categoria + "titulo " + titulo + "Corpo" + corpo)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/cadmateria",CadastrarMateria),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()

    #Curl testes
    #curl -d "categoria=esportes&titulo='Botafogo campeao'&corpo='Corpo de toda a materia'" -X POST http://localhost:80/admin
