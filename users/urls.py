from .views import HomeView
homeview = HomeView()

mount = "/"

# routes = {
#	 '/': ,
#	 "/new": ,
# }
routes = {}
# routes[404] = (homeview.error_404)
routes[""] = {
	"": (homeview.index, ["GET", "POST"], "homepage"),
	"/<id:int>": (homeview.index, ["GET", "POST"], "homepage")
}
routes["/new"] = (homeview.new, "GET", "new-item")