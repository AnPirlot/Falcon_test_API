import falcon
import utils.json
import utils.storage

storage = utils.storage.Storage()

class Collection(object):

    @falcon.before(utils.json.RequireJSON.process_request)
    @falcon.before(utils.json.JSONTranslator.process_request)
    def on_get(self, req, resp):
        resp.body = '{"message": "Here are your tasks!"}'
        resp.status = falcon.HTTP_200

    @falcon.before(utils.json.RequireJSON.process_request)
    @falcon.before(utils.json.JSONTranslator.process_request)
    def on_post(self, req, resp):

        task_dict = req.context['content']
        self._store(task_dict)

        resp.status = falcon.HTTP_201


    def _store(self, task_dict):
        try:
            task_name = task_dict['name']
            task_begin_date = task_dict['begin_date']
            task_end_date = task_dict['end_date']
            task_info = "name:%s ; begin:%s ; end:%s \n" % (task_name, task_begin_date, task_end_date)

            with open("Tasks.txt", "a") as text_file:
                text_file.write("{0}".format(task_info))

            insert = """INSERT INTO "Tasks"."Tasks" ("Name", "Begin_date", "End_date") VALUES ('%s', '%s', '%s')""" % (
            task_name, task_begin_date, task_end_date)
            storage.set(insert)

        except Exception as exception:
            with open("Errorlog.txt", "a") as text_file:
                text_file.write("\n In tasks.tasks.Collection._store: {0}".format(exception))

