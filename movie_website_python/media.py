import webbrowser

class Movie():
	#定义 Movie 这个类的初始函数。此函数将接收 5 个参数，并将后 4 个参数值绑定给第一个参数————即调用此初始函数的 Movie 类的实例本身
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	#此函数接收一个参数————Movie 类的实例本身，并打开浏览器，打开地址是实例本身所有的 trailer_youtube_url 这个属性所指向的 URL
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
