
import jinja2
import os
import sys
import requests
import tornado.ioloop
import tornado.web
import boto3
import hashlib


hash_object=hashlib.sha256(os.urandom(256))
hex_dig=hash_object.hexdigest()
print(hex_dig)

#MessageGroupId='cf066e9b6526e7e7b8aed748109b4c2bf04d015cbd04422ca2242ca837d53e43',


sqs = boto3.client('sqs',region_name='us-east-1',aws_access_key_id='AKIAXT3YH346U7XUH4WE',aws_secret_access_key='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')
queue_url = 'https://sqs.us-east-1.amazonaws.com/523701313341/curso-amazon-globo.fifo'
# Send message to SQS queue
response = sqs.send_message(
    MessageGroupId=str(hex_dig),
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
        'Subindo uma nova msg'
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
    #acess key  AKIAXT3YH346U7XUH4WE
    #secret access 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

    #MessageGroupId='d2c701fwe3',
    # tem que gerar um sha256 para cada msg