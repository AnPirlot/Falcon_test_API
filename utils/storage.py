import psycopg2
import utils.conf

host = utils.conf.host
dbname = utils.conf.dbname
user = utils.conf.user
password = utils.conf.password

CONNECTION = ''

class Storage(object):

    def __init__(self):
        # Define our connection string
        conn_string = "host=%s dbname=%s user=%s password=%s" % (host, dbname, user, password)

        # get a connection, if a connection cannot be made an exception will be raised here
        try:
            self.CONNECTION = psycopg2.connect(conn_string)
        except Exception as exception:
            with open("Errorlog.txt", "a") as text_file:
                text_file.write("\n In utils.storage.Storage.__init__: {0}".format(exception))

    def set(self, query):
        cursor = self.CONNECTION.cursor()
        cursor.execute(query)
        self.CONNECTION.commit()