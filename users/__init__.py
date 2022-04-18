from wsgic import WSGIApp

class UsersApp(WSGIApp):
	def __init__(self):
		super().__init__(__package__)

def get_app():
	app = UsersApp()
	return app