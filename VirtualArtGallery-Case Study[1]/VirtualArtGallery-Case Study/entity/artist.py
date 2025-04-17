class Artist:
    def __init__(self, artist_id, name, biography, birth_date, nationality, website, contact_info):
        self.artist_id = artist_id
        self.name = name
        self.biography = biography
        self.birth_date = birth_date
        self.nationality = nationality
        self.website = website
        self.contact_info = contact_info

    def get_artist_id(self):
        return self.artist_id

    def get_name(self):
        return self.name

    def get_biography(self):
        return self.biography

    def get_birth_date(self):
        return self.birth_date

    def get_nationality(self):
        return self.nationality

    def get_website(self):
        return self.website

    def get_contact_info(self):
        return self.contact_info
