class Artwork:
    def __init__(self, artwork_id, title, artist_id, category_id, creation_date, medium, image_url):
        self.artwork_id = artwork_id
        self.title = title
        self.artist_id = artist_id
        self.category_id = category_id
        self.creation_date = creation_date
        self.medium = medium
        self.image_url = image_url

    def get_artwork_id(self):
        return self.artwork_id

    def get_title(self):
        return self.title

    def get_artist_id(self):
        return self.artist_id

    def get_category_id(self):
        return self.category_id

    def get_creation_date(self):
        return self.creation_date

    def get_medium(self):
        return self.medium

    def get_image_url(self):
        return self.image_url
