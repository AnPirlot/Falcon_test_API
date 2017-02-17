import falcon

import tasks.tasks
import utils

ALLOWED_ORIGINS = utils.conf.allowed_hosts # Or load this from a config file

class CorsMiddleware(object):

    def process_request(self, request, response):
        origin = request.get_header('Origin')
        if origin in ALLOWED_ORIGINS:
            response.set_header('Access-Control-Allow-Origin', origin)

api = application = falcon.API(middleware=[CorsMiddleware()])

task_collection = tasks.tasks.Collection()

api.add_route('/tasks', task_collection)