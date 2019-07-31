# -*- coding: utf-8 -*-

from bottle import response, request, static_file
from bottle import Bottle
import bottle
from bson import json_util
from functools import wraps
from cheroot.wsgi import Server as WSGIServer
import os
import requests
import wikipedia
import json

app = Bottle()

SESSIONS = dict()

curr_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.abspath(os.path.join(curr_dir, os.pardir))


def enable_cors(fn):
    '''
    Setting headers for the app
    '''
    @wraps(fn)
    def _enable_cors(*args, **kwargs):
        # set CORS headers, do not double what is defined in vhosts
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@app.route('/')
@enable_cors
def index():
    return 'Here is the home';

@app.route('/todays-word/<search_text>')
@enable_cors
def wikipediaSearch(search_text):
    response_string = ""
    wikipedia.set_lang("en")
    search_response = wikipedia.search(search_text)
    if not search_response:
        response_string = "this word is not registered."
        return response_string
    try:
        wiki_page = wikipedia.page(search_response[0])
    except Exception as e:
        response_string = "error \n{}\n{}".format(e.message, str(e))
        return response_string
    wiki_content = wiki_page.content
    todays_word = "Today's word: "+ search_text
    explanation = wiki_content[0:wiki_content.find(".")]
    url = "here is the link：" + wiki_page.url
    return json.dumps({"word":todays_word, "explanation": explanation, "url":url})




@app.route('/test')
@enable_cors
def test():
    response = requests.get(
        'https://api.github.com/search/repositories',
        params={'q': 'requests+language:python'},
    )

    # Inspect some attributes of the `requests` repository
    json_response = response.json()
    repository = json_response['items'][0]
    return 'It works yann coucou ' + repository["description"];


@app.route('/static/<filename>')
@enable_cors
def server_static(filename):
    return static_file(filename, root='/var/www/app/static')


if __name__ == '__main__':
    server = WSGIServer(('0.0.0.0', 8080),
                        app,
                        numthreads=30)
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
