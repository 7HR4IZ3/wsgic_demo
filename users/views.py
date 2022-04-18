import json
from wsgic.backend import request, response

class HomeView():
	def __init__(self, **kwargs):
		self.model = {"users": [
			{"name": "Azeez", "age": 19, "color": "blue"},
			{"name": "Thraize", "age": 18, "color": "green"}
		]}

	def index(self, id=None):
		response.set_header("Content-type", "application/json")
		data = self.model if not id else self.model["users"][id-1]
		return json.dumps(data, indent=4)

	def new(self):
		self.model["users"].append({"name": request.GET.name, "age": request.GET.age, "color": request.GET.color})
		return "Added product"

