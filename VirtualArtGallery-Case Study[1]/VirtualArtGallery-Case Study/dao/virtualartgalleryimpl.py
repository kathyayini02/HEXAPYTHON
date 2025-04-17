from dao.ivirtualartgallery import IVirtualArtGallery
from util.db_connection import DBConnection

class VirtualArtGalleryImpl(IVirtualArtGallery):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    # ✅ Add Artwork
    def add_artwork(self, artwork):
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Artworks (Title, ArtistID, CategoryID, CreationDate, Medium, ImageURL) 
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                artwork.get_title(),
                artwork.get_artist_id(),
                artwork.get_category_id(),
                artwork.get_creation_date(),
                artwork.get_medium(),
                artwork.get_image_url()
            ))
            self.conn.commit()
            print("✔ Artwork added successfully.")
        except Exception as e:
            print(f"❌ Error adding artwork: {e}")

    # ✅ Get Artwork by ID
    def get_artwork_by_id(self, artwork_id):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Artworks WHERE ArtworkID = ?"
            cursor.execute(query, (artwork_id,))
            artwork = cursor.fetchone()
            return artwork or f"❌ No artwork found with ID {artwork_id}."
        except Exception as e:
            print(f"❌ Error retrieving artwork: {e}")
            return None

    # ✅ Remove Artwork
    def remove_artwork(self, artwork_id):
        try:
            cursor = self.conn.cursor()
            # Check existence
            cursor.execute("SELECT COUNT(*) FROM Artworks WHERE ArtworkID = ?", (artwork_id,))
            if cursor.fetchone()[0] == 0:
                print(f"❌ Error: Artwork with ID {artwork_id} does not exist.")
                return

            # Delete from dependencies first
            cursor.execute("DELETE FROM User_Gallery_Artworks WHERE ArtworkID = ?", (artwork_id,))
            cursor.execute("DELETE FROM User_Favorite_Artwork WHERE ArtworkID = ?", (artwork_id,))
            cursor.execute("DELETE FROM Artworks WHERE ArtworkID = ?", (artwork_id,))
            self.conn.commit()
            print(f"✔ Artwork with ID {artwork_id} removed successfully.")
        except Exception as e:
            print(f"❌ Error removing artwork: {e}")

    # ✅ Update Artwork
    def update_artwork(self, artwork):
        try:
            cursor = self.conn.cursor()
            query = """
                UPDATE Artworks 
                SET Title = ?, ArtistID = ?, CategoryID = ?, CreationDate = ?, Medium = ?, ImageURL = ?
                WHERE ArtworkID = ?
            """
            cursor.execute(query, (
                artwork.get_title(),
                artwork.get_artist_id(),
                artwork.get_category_id(),
                artwork.get_creation_date(),
                artwork.get_medium(),
                artwork.get_image_url(),
                artwork.get_artwork_id()
            ))
            self.conn.commit()
            print("✔ Artwork updated successfully.")
        except Exception as e:
            print(f"❌ Error updating artwork: {e}")

    # ✅ Search Artworks
    def search_artworks(self, keyword):
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM Artworks WHERE Title LIKE ? OR Medium LIKE ?"
            cursor.execute(query, (f'%{keyword}%', f'%{keyword}%'))
            results = cursor.fetchall()
            return results if results else "❌ No artworks found matching the keyword."
        except Exception as e:
            print(f"❌ Error searching artworks: {e}")
            return None

    # ✅ Get All Artworks
    def get_all_artworks(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Artworks")
            results = cursor.fetchall()
            return results if results else "❌ No artworks found."
        except Exception as e:
            print(f"❌ Error retrieving artworks: {e}")
            return None

    # ✅ Get All Artists
    def get_all_artists(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Artists")
            results = cursor.fetchall()
            return results if results else "❌ No artists found."
        except Exception as e:
            print(f"❌ Error retrieving artists: {e}")
            return None

    # ✅ Get All Categories
    def get_all_categories(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Categories")
            results = cursor.fetchall()
            return results if results else "❌ No categories found."
        except Exception as e:
            print(f"❌ Error retrieving categories: {e}")
            return None

    # ✅ Create Personal Gallery
    def create_user_gallery(self, user_id, name, description):
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO User_Galleries (UserID, Name, Description) 
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (user_id, name, description))
            self.conn.commit()
            print("✔ Personal Gallery created successfully.")
        except Exception as e:
            print(f"❌ Error creating personal gallery: {e}")

    # ✅ Get User's Personal Galleries
    def get_user_galleries(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM User_Galleries WHERE UserID = ?", (user_id,))
            results = cursor.fetchall()
            return results if results else "❌ No galleries found for this user."
        except Exception as e:
            print(f"❌ Error retrieving personal galleries: {e}")
            return None

    # ✅ Add Artwork to Personal Gallery
    def add_artwork_to_gallery(self, gallery_id, artwork_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO User_Gallery_Artworks (GalleryID, ArtworkID) 
                VALUES (?, ?)
            """, (gallery_id, artwork_id))
            self.conn.commit()
            print("✔ Artwork added to gallery successfully.")
        except Exception as e:
            print(f"❌ Error adding artwork to gallery: {e}")

    # ✅ Remove Artwork from Personal Gallery
    def remove_artwork_from_gallery(self, gallery_id, artwork_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                DELETE FROM User_Gallery_Artworks 
                WHERE GalleryID = ? AND ArtworkID = ?
            """, (gallery_id, artwork_id))
            self.conn.commit()
            print("✔ Artwork removed from gallery successfully.")
        except Exception as e:
            print(f"❌ Error removing artwork from gallery: {e}")

    # ✅ Get All Artworks in a Personal Gallery
    def get_gallery_artworks(self, gallery_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT a.ArtworkID, a.Title, a.Medium, a.ImageURL 
                FROM User_Gallery_Artworks uga
                JOIN Artworks a ON uga.ArtworkID = a.ArtworkID
                WHERE uga.GalleryID = ?
            """, (gallery_id,))
            results = cursor.fetchall()
            return results if results else "❌ No artworks found in this gallery."
        except Exception as e:
            print(f"❌ Error retrieving artworks in gallery: {e}")
            return None

    # ✅ Delete Personal Gallery
    def delete_user_gallery(self, gallery_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM User_Gallery_Artworks WHERE GalleryID = ?", (gallery_id,))
            cursor.execute("DELETE FROM User_Galleries WHERE GalleryID = ?", (gallery_id,))
            self.conn.commit()
            print("✔ Personal Gallery deleted successfully.")
        except Exception as e:
            print(f"❌ Error deleting gallery: {e}")
