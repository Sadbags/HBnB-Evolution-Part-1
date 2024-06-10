from basemodel import BaseModel

class Place(BaseModel):
    def __init__(self, name, location, owner, description="", address="", city=None, price_per_night=0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.location = location
        self.owner = owner
        self.descripton = description
        self.address = address
        self.city = city
        self.price_per_night = price_per_night
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenities(self, amenity):
        self.amenities.append(amenity)
