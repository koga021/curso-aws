
import jinja2
import os
import sys
import requests
import tornado.ioloop
import tornado.web
import boto3

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/523701313341/curso-amazon-globo.fifo'
# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])


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
