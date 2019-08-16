import re
import json
from googlesearch import search

def html_result(result):
    html = '<html><body><h1>Search Results</h1>'
    for r in result:
        html += '<p><a href=%s>%s</a>' % (r, r)
    html += '</body></html>'
    return html

def google_search(query = '"cancer" "aws" devops -careers -jobs'):
    results = list(search(query=query, lang='en', num=10, stop=10, pause=1, only_standard=True))

    return html_result(query_results)

def search_handler(event, context):
    if event['httpMethod'] == 'GET':
        try:
            return {'statusCode': 200, 'body': json.dumps(google_search())}
        except:
            return {'statusCode': 400, 'body': 'bad request'}
