from wsgic.base.models import Model

class Product(Model):
	def __init__(self):
		super().__init__()
		self.column('id', "integer primary key")
		# self.column('icon', "text", null=True)
		self.column('name', 'text', null=True)
		self.column('category', 'text')
		self.column('date', "date")
		self.column('experience', "text", null=True)
		# self.column('work_level', 'text', null=True)
		# self.column('employee_type', 'text', null=True)
		# self.column('offer_salary', 'text', null=True)
		# self.column('overview', "text", null=True)
		# self.column('description', "text", null=True)
		self.create()