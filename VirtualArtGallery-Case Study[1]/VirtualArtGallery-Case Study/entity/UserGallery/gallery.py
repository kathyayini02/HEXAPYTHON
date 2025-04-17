class UserGallery:
    def __init__(self, gallery_id, user_id, name, description):
        self.__gallery_id = gallery_id
        self.__user_id = user_id
        self.__name = name
        self.__description = description

    # Getters
    def get_gallery_id(self):
        return self.__gallery_id

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description
