import falcon

import tasks.tasks

api = application = falcon.API()

task_collection = tasks.tasks.Collection()

api.add_route('/tasks', task_collection)