class User:
    def __init__(self, user_id, username, password_hash, email, first_name, last_name, date_of_birth, profile_picture):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.profile_picture = profile_picture

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    def get_password_hash(self):
        return self.password_hash

    def get_email(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_profile_picture(self):
        return self.profile_picture
