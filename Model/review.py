from basemodel import BaseModel

class Review(BaseModel):
    """ Review class that inherits from BaseModel. Represents a review for a place. """
    def __init__(self, rating, content, author, place, **kwargs):
        """ Initializes the Review with the given attributes """
        super().__init__(**kwargs)
        self.rating = rating
        self.content = content
        self.author = author
        self.place = place
