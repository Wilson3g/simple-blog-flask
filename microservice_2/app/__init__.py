from flask import Flask, request
from flask_restful import Resource, Api
from elasticsearch import Elasticsearch
import datetime

app = Flask(__name__)
api = Api(app)
es = Elasticsearch('http://localhost:9200')

class Post(Resource):
    def get(self):
        posts = es.search(index='posts')
        return {'posts': posts['hits']['hits']}

    def post(self):
        now = str(datetime.date.today())
        print(request.json.values())

        if len(request.json) < 4 or '' in request.json.values():
            return {'success': False, 'message': 'Informe todos os campos obrigatórios'}, 401

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

class ManipulatePosts(Resource):
    def get(self, query):
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                }
            }
        }

        posts = es.search(index='posts', body=body)
        return {'posts': posts['hits']['hits']}

    def put(self, query):
        posts = es.search(index='posts')
        return {'posts': posts['hits']['hits']}

    def delete(self, query):
        posts = es.search(index='posts')
        return {'posts': posts['hits']['hits']}

api.add_resource(Post, '/post')
api.add_resource(ManipulatePosts, '/post/<string:query>')

if __name__ == "__main__":
    app.run(port=5000, debug=True)