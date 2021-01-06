from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.input.shape import ShapeRect


class rooot(BoxLayout):
#	def on_touch_move(self,touch):
#		if isinstance(touch.shape, ShapeRect):
#			print('my touch size is good',(touch.shape.width, touch.shape.height))

#	def touch(self,touch):
#		if touch.is_double_tap:
#			print("double tap is ")
#			print('intervial is :', touch.double_tap_time)
#			print('distance is between is ', touch.double_tap_distance)


	def on_touch_down(self,touch):
		if self.collide_point(*touch.pos):
			touch.grab(self)
			return True

	def on_touch_up(self,touch):
		if touch.grab_current is self:
#			print("hello word")
			touch.ungrab(self)
			return True





class TestApp(App):
	def build(self):
		return rooot()

if __name__ == '__main__':
	TestApp().run()
