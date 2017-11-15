#引入外部文件，以期能使用文件中的类的一些方法
import fresh_tomatoes
import media

#实例化 5 个 Movie 类的实例，并分别传入其所需的 5 个参数
Interstellar = media.Movie("Interstellar",
						"Sometime in the 21st century, a series of crop blights and dust storms on Earth threaten humanity's survival...",
						"https://i.ytimg.com/vi/Df7IEKqimOY/movieposter.jpg",
						"https://www.youtube.com/watch?v=0vxOhd4qlnA")

dangal = media.Movie("dangal",
						"Dangal (English: Wrestling competition) is a 2016 Indian Hindi-language biographical sports drama film, loosely based on the Phogat family, telling the story of Mahavir Singh Phogat, an amateur wrestler, who trains his daughters Geeta Phogat and Babita Kumari to be India's first world-class female wrestlers.",
						"https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
						"https://www.youtube.com/watch?v=x_7YlGv9u1g")

The_Shawshank_Redemption = media.Movie("The_Shawshank_Redemption",
						"The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont, based on the Stephen King novella Rita Hayworth and Shawshank Redemption. It tells the story of banker Andy Dufresne (Tim Robbins), who is sentenced to life in Shawshank State Penitentiary for the murder of his wife and her lover, despite his claims of innocence. Over the following two decades, he befriends a fellow prisoner, contraband smuggler Ellis 'Red' Redding (Morgan Freeman), and becomes instrumental in a money laundering operation led by the prison warden Samuel Norton (Bob Gunton).",
						"https://static.rogerebert.com/uploads/movie/movie_poster/the-shawshank-redemption-1994/large_9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg",
						"https://www.youtube.com/watch?v=6hB3S9bIaco")

cinderella_man = media.Movie("cinderella_man",
						"Cinderella Man is a 2005 American drama film by Ron Howard, titled after the nickname of heavyweight boxing champion James J. Braddock and inspired by his life story.",
						"https://images-na.ssl-images-amazon.com/images/I/51kUhYpYkNL._SY445_.jpg",
						"https://www.youtube.com/watch?v=-3ywc_7_IE8")

inception = media.Movie("inception",
						"Inception is a 2010 science fiction film written, co-produced, and directed by Christopher Nolan, and co-produced by Emma Thomas. The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious, and is offered a chance to have his criminal history erased as payment for a seemingly impossible task: 'inception', the implantation of another person's idea into a target's subconscious.",
						"https://www.goldenglobes.com/sites/default/files/films/inception.jpg",
						"https://www.youtube.com/watch?v=YoHD9XEInc0")

#将以上 5 个实例放入一个数组中，供 fresh_tomatoes 文件中 open_movies_page 方法所调用
movies = [Interstellar, dangal, The_Shawshank_Redemption, cinderella_man, inception]
fresh_tomatoes.open_movies_page(movies)
