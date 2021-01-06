#import kivy
from kivy.app import App
from kivy.uix.label import Label

class myapp(App):
#	def build(self):
#		return Label(text="Welcome to ns world")
	def __init__(self,**kwargs):
		self.register_event_type('on_test')
		super(myapp,self).__init__(**kwargs)


	def do(self,value):
		self.dispatch('on_test',value)

	def on_test(self,*args):
		print("i am diispath", args)
if __name__=='__main__':
	myapp().run()
