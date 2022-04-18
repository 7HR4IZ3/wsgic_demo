from .views import HomeView, ArticleView

hv = HomeView()
av = ArticleView()

mount = "/"

routes = {}
routes['/'] = (hv.index, ["GET", "POST"], "homepage")
routes["/test"] = (hv.test, "GET", "async")

routes["/users"] = "users"
routes['/django'] = "test::django"
routes["/flask"] = "flas.app::flask"
# routes["/pyramid"] = "pyr.app::pyramid"

routes["/article"] = (av, "GET")