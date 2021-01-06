from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class login(GridLayout):
	def __init__(self,**kwargs):
		super(login,self).__init__(**kwargs)
		self.cols=2
		self.add_widget(Label(text='username'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True,multiline=False)
		self.add_widget(self.password)

class myapp(App):
	def build(self):
		return login()

if __name__ == '__main__':
	myapp().run()

