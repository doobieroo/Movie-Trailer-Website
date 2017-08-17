import media
import fresh_tomatoes

#Create new instances of class Movie for each movie in the web page
the_holiday = media.Movie("The Holiday",
                        "Two women meet their dream man.",
                        "https://upload.wikimedia.org/wikipedia/en/6/60/Theholidayposter.jpg",
                        "https://www.youtube.com/watch?v=JGBl5FxOrUQ")


idiocracy = media.Movie("Idiocracy",
                     "The world has gotten dumb, really dumb.",
                     "https://upload.wikimedia.org/wikipedia/en/6/6b/Idiocracy_movie_poster.jpg",
                     "https://www.youtube.com/watch?v=ztSngdklb5g")



dirty_dancing = media.Movie("Dirty Dancing",
                            "Girl meets inappropriate soul mate - grows up.",
                            "https://upload.wikimedia.org/wikipedia/en/0/00/Dirty_Dancing.jpg",
                            "https://www.youtube.com/watch?v=eIcmQNy9FsM")


pretty_woman = media.Movie("Pretty Woman",
                           "Guy meets girl from wrong side of town, love happens.",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/Pretty_woman_movie.jpg",
                           "https://www.youtube.com/watch?v=Ng2hEIWVqqo")

sixteen_candles = media.Movie("Sixteen Candles",
                              "Awkward teenage romance of the 80's.",
                              "https://upload.wikimedia.org/wikipedia/en/3/34/Sixteen_Candles.jpg",
                              "https://www.youtube.com/watch?v=HGLtBJupFFM")


american_pie = media.Movie("American Pie",
                           "Teen sex comedy featuring pie and flutes.",
                           "https://upload.wikimedia.org/wikipedia/en/c/c8/American_Pie1.jpg",
                           "https://www.youtube.com/watch?v=RnWpLaN84uM")

#create list of all movie objects
movies = [the_holiday,idiocracy,dirty_dancing, pretty_woman, sixteen_candles, american_pie]

#call function from fresh_tomatoes.py to create an html file for display
fresh_tomatoes.open_movies_page(movies)

