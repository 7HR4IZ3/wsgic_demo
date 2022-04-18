# wsgic_demo
wsgic demo app
just run main.py

# Dispatched wsgi apps files
 `web`, `users` -> Bottle App

`flas.py` -> flask app

`test`, `main` -> Django app and config(test)

`pyr.py` -> Pyramid app

# How to dispatch wsgi app
`web/urls.py`:
```python

from .views import HomeView, ArticleView

hv = HomeView()
av = ArticleView()

mount = "/"

# Routhing scheme for wsgic
routes = {}
routes['/'] = (hv.index, ["GET", "POST"], "homepage") # routes[route] = (function, method(s), name, apply(plugin))
routes["/test"] = (hv.test, "GET", "async")

routes["/users"] = "users::bottle" # bottle wsgi app
routes['/django'] = "test::django" # django wsgi app
routes["/flask"] = "flas.app::flask" # flask wsgi app
routes["/pyramid"] = "pyr.app::pyramid" # pyramid wsgi app

routes["/article"] = (av, "GET")
