from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


class rootwidget(BoxLayout):
	def __init__(self,**kwargs):
		super(rootwidget,self).__init__(**kwargs)
		self.add_widget(Button(text='btn 1'))
		cb = CustomBtn()
		cb.bind(pressed=self.btn_pressed)
		self.add_widget(cb)
		self.add_widget(Button(text='btn 2'))

	def btn_pressed(self,instance,pos):
		print('pos: root:{pos}'.format(pos=pos))

class CustomBtn(Widget):
	pressed = ListProperty([0,0])

	def on_touch(self,touch):
		if self.collide_point(*touch.pos):
			self.pressed = touch.pos
			return True
		return super(CustomBtn,self).on_touch(touch)

	def on_pressed(self,instance,pos):
		print('pressed at {pos}'.format(pos=pos))

class Test(App):
	def build(self):
		return rootwidget()

if __name__ == '__main__':
	Test().run()
