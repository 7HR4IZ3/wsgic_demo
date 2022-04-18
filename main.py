

# if __name__ == '__main__':
# 	import sys, os;os.environ["gx_settings_module"] = "settings"
# 	from wsgic.server.helpers import parse_args; parse_args(sys.argv)

def start_app(name):
	import os
	files = {
		"__init__": f"""from wsgic import WSGIApp

class {name.title()}App(WSGIApp):
	def __init__(self):
		super().__init__(__package__)

def get_app():
	app = {name.title()}App()
	return app

def run(**kw):
	get_app().run(**kw)
""",
		"views" : """from wsgic.base.views import View

class HomeView(View):
	def __init__(self):
		super().__init__(self)

	def index(self):
		return "Homepage"
""",
		"urls" : """from .views import HomeView
hv = HomeView()

mount = "/"

routes = {}
routes['/'] = (hv.index, ["GET", "POST"], "homepage")
""",
		"models" : """from wsgic.base.models import Model, Field

class Blog(Model):
	def __init__(self):
		super().__init__()
		self.column.name = Field(type="text")
		self.column.title = Field(type="text")
		self.column.rating = Field(type="integer", default=1)
		self.create()
""",
		"controllers" : """
""",
		"helpers": """
"""
	}
	os.system(f"mkdir {name}")
	for m in files:
		try:
			print(f"Generating File: {m}.py")
			with open(f"{name}/{m}.py", "x") as file:
				file.write(files[m])
		except FileExistsError:
			print("File {m}.py Already Exists")
			pass
	print(f"Created WSGI App: {name}")


from web import run

run()