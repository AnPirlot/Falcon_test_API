import falcon
import sys
import utils.json


class Collection(object):

    @falcon.before(utils.json.RequireJSON.process_request)
    @falcon.before(utils.json.JSONTranslator.process_request)
    def on_post(self, req, resp):

        task_dict = req.context['content']

        try:
            task_name = task_dict['name']
            task_begin_date = task_dict['begin_date']
            task_end_date = task_dict['end_date']
            task_info = "name:%s ; begin:%s ; end:%s \n" % (task_name, task_begin_date, task_end_date)

            with open("Tasks.txt", "a") as text_file:
                text_file.write("{0}".format(task_info))

        except:
            exception = sys.exc_info()[0]
            with open("Tasks.txt", "a") as text_file:
                text_file.write("{0}".format(exception))

        resp.status = falcon.HTTP_201
