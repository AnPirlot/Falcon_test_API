# Small REST api using Falcon
This repository holds the code to set up a small REST api. This is part of my little server system. Variables should be stored in utils/conf.py. This can also be installed for python3 using pip3


## Installation

### Install falcon
http://falcon.readthedocs.io/en/stable/user/install.html
```
pip install falcon

```

### Install uwsgi
https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
```
pip install uwsgi
```

### Install psycopg2
When using psycopg2 for a direct connection to a postgresql db
http://initd.org/psycopg/docs/install.html#binary-install-from-pypi
```
pip install psycopg2
```

## Running the api via uwsgi
uwsgi --http :8080 --wsgi-file app.py
