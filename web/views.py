from wsgic.base.views import View, Single
# from wsgic.backend import request, jinja2_template as render
# from wsgic.server.helpers import get_config

# from .helpers import run_code

class HomeView(View):
	def __init__(self):
		super().__init__(self)

	def index(self):
		return "Homepage"

	def test(self):
		yield "Getting Data"
		data = {}
		if data != {}:
			return data
		else:
			yield "No data in database"

class ArticleView(Single):
	def __init__(self):
		super().__init__()

	def get(self, request):
		return f"Getting Data on id {request.GET.id}"
