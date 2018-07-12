import hug
from hug_explainable import middleware, explain

api = hug.API(__name__)
CODE_URLS = {'/hug_explainable/': 'https://github.com/timothycrosley/hug_explainable/blob/develop/hug_explainable/',
             'examples/': 'https://github.com/timothycrosley/hug_explainable/blob/develop/examples/'}
middleware.init(api, code_urls=CODE_URLS)
route = hug.http().suffixes('.explain.json', '.explain.html')


@route.get()
def my_code(explain: explain):
    with explain("Doing maths", 10):
        answer = 10 + 10
    with explain("Doing maths", 10):
        answer = 10 + 10
    with explain("Doing maths", {'numbers': [1,2,3,4], 'booleans': {'true': True, 'false': False}}):
        answer = 10 + 10
    with explain("Doing maths", 10):
        answer = 10 + 10
        return {'answer': answer, 'explanation': explain}
