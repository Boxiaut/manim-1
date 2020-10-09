from manim import *

class MoreShapes(Scene):
	def construct(self):
		circles = []
		for i in range(-4,5):
			circle = Circle(color=GOLD).move_to(i*RIGHT)
			circles.append(circle)

		for i in range(-4,5):
			self.play(FadeIn(circles[i+4]),time=.1)
