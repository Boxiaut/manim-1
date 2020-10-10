from manimlib.imports import *

class MoreShapes(Scene):
	def construct(self):
		mobjects = VGroup(
			Dot(),
			TexMobject("x")
		)
		mobjects.arrange_submobjects(RIGHT,buff=2)

		mobject_or_coord = [
			*mobjects,                    # Mobjects: Dot and "x"
			mobjects.get_right()+RIGHT*2  # Coord
		]

		colors=[GRAY,RED,BLUE]

		self.add(mobjects)

		for obj,color in zip(mobject_or_coord,colors):
			self.play(FocusOn(obj,color=color))

		self.wait(0.3)