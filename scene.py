from manimlib.imports import *

class MoreShapes(Scene):
	def construct(self):
		text = TextMobject("ShowIncreasingSubsets")
		text.set_width(6)
		text1 = TextMobject("LastIncreasingSubsets")
		text1.set_width(6)
		text1.move_to(TOP)
		self.wait()
		self.play(FadeInFromLarge(
			text,
			run_time=0.4, 
			rate_func=rush_into
		))
		
		self.play(FadeOut(text, taget_mobject=text1))
		self.wait()