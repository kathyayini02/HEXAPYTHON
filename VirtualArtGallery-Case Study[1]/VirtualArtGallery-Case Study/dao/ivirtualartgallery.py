from abc import ABC, abstractmethod

class IVirtualArtGallery(ABC):

    @abstractmethod
    def add_artwork(self, artwork):
        pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id):
        pass

    @abstractmethod
    def remove_artwork(self, artwork_id):
        pass

    @abstractmethod
    def update_artwork(self, artwork):
        pass

    @abstractmethod
    def search_artworks(self, keyword):
        pass

    @abstractmethod
    def get_all_artworks(self):
        pass

    @abstractmethod
    def get_all_artists(self):
        pass

    @abstractmethod
    def get_all_categories(self):
        pass

    # ✅ Personal Gallery Methods
    @abstractmethod
    def create_user_gallery(self, user_id, name, description):
        pass

    @abstractmethod
    def get_user_galleries(self, user_id):
        pass

    @abstractmethod
    def add_artwork_to_gallery(self, gallery_id, artwork_id):
        pass

    @abstractmethod
    def remove_artwork_from_gallery(self, gallery_id, artwork_id):
        pass

    @abstractmethod
    def get_gallery_artworks(self, gallery_id):
        pass

    @abstractmethod
    def delete_user_gallery(self, gallery_id):
        pass
