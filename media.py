import webbrowser


# This class provides a way to store movie related information.
class Movie():

    # Initialize this class with the variables you'll be passed.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    '''Using the library webbrowser - open a new window and play the YouTube
    trailer.'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
