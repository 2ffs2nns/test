import re
import json
from googlesearch import search

def html_result(result):
    html = '<h1>Search Results</h1>'
    for r in result:
        html += '<p><a href=%s>%s</a>' % (r, r)
    return html

def google_search(query = '"cancer" "aws" devops -careers -jobs'):
    query_results = list(search(query=query, lang='en', num=10, stop=10, pause=1, only_standard=True))

    return html_result(query_results).strip('"')

def search_handler(event, context):
    if event['httpMethod'] == 'GET':
        try:
            return {'statusCode': 200, 'body': json.dumps(google_search()), 'headers': {'Content-Type': 'text/html; charset=utf-8'}}
        except:
            return {'statusCode': 400, 'body': 'bad request'}
