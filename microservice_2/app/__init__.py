from flask import Flask, request
from flask_restful import Resource, Api
from elasticsearch import Elasticsearch
import datetime

app = Flask(__name__)
api = Api(app)
es = Elasticsearch('http://localhost:9200')

class Post(Resource):
    def get(self, query):

        posts = es.search(index='posts')
        return {'posts': posts['hits']['hits']}
    
    # def get(self, query):
    #     posts = es.search(index='posts')
    #     return {'posts': posts['hits']['hits']}

    def post(self, query):
        now = str(datetime.date.today())

        id = request.json['user_id'],
        title = request.json['title'],
        content = request.json['content'],
        author = request.json['author'],

        body = {
            'id': id,
            'title': title,
            'content': content,
            'author': author,
            'created_at': now.replace('-', '/'),
            'updated_at': now.replace('-', '/')
        }
        
        posts = es.index(index='posts', op_type='create', body=body)
        
        return {'success': True}, 201

    def put(self, query):
        posts = es.search(index='posts')
        return {'posts': posts['hits']['hits']}

    def delete(self, query):
        posts = es.search(index='posts')
        return {'posts': posts['hits']['hits']}

api.add_resource(Post, '/post/<string:query>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)