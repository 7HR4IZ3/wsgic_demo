from wsgic import WSGIApp

class WebApp(WSGIApp):
	def __init__(self):
		super().__init__(__package__)

def get_app():
	app = WebApp()
	return app

def run(**kw):
	get_app().run(**kw)