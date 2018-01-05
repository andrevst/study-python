import webbrowser

class Movie():
    """ This class create a movie and shows its trailer. """

    def __init__ (self,title,year,sinopse,poster_img_url,trailer_youtube_url):
        self.title = title
        self.year = year
        self.sinopse = sinopse
        self.poster_img_url = poster_img_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
