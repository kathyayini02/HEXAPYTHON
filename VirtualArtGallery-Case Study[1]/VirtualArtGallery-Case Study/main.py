from dao.virtualartgalleryimpl import VirtualArtGalleryImpl
from entity.artwork import Artwork

def main():
    gallery_service = VirtualArtGalleryImpl()

    while True:
        print("\n Virtual Art Gallery System")
        print("1. Add Artwork")
        print("2. View Artwork by ID")
        print("3. Delete Artwork")
        print("4. View All Artworks  ")
        print("5. Create Personal Gallery")
        print("6. View My Galleries")
        print("7. Add Artwork to My Gallery")
        print("8. Remove Artwork from My Gallery")
        print("9. View Artworks in My Gallery")
        print("10. View All Artists")
        print("11. View All Categories")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            artist_id = input("Enter artist ID: ")
            category_id = input("Enter category ID: ")
            creation_date = input("Enter creation date (YYYY-MM-DD): ")
            medium = input("Enter medium: ")
            image_url = input("Enter image URL: ")
            
            artwork = Artwork(None, title, artist_id, category_id, creation_date, medium, image_url)
            gallery_service.add_artwork(artwork)

        elif choice == "2":
            artwork_id = input("Enter artwork ID: ")
            artwork = gallery_service.get_artwork_by_id(artwork_id)
            if artwork:
                print("\n Artwork Details:")
                print(f"ID: {artwork[0]}, Title: {artwork[1]}, Artist ID: {artwork[2]}, Category ID: {artwork[3]}")
                print(f"Date: {artwork[4]}, Medium: {artwork[5]}, Image URL: {artwork[6]}")
            else:
                print("❌ No artwork found with this ID.")

        elif choice == "3":
            artwork_id = input("Enter artwork ID: ")
            gallery_service.remove_artwork(artwork_id)

        elif choice == "4":
            artworks = gallery_service.get_all_artworks()
            if artworks:
                print("\n All Artworks:")
                for art in artworks:
                    print(f"ID: {art[0]}, Title: {art[1]}, Artist ID: {art[2]}, Category ID: {art[3]}, Date: {art[4]}, Medium: {art[5]}, Image: {art[6]}")
            else:
                print("❌ No artworks available.")

        elif choice == "5":
            user_id = input("Enter User ID: ")
            name = input("Enter Gallery Name: ")
            description = input("Enter Gallery Description: ")
            gallery_service.create_user_gallery(user_id, name, description)

        elif choice == "6":
            user_id = input("Enter User ID: ")
            galleries = gallery_service.get_user_galleries(user_id)
            if galleries:
                print("\n Your Galleries:")
                for gallery in galleries:
                    print(f"ID: {gallery[0]}, Name: {gallery[1]}, Description: {gallery[2]}")
            else:
                print("❌ No galleries found for this user.")

        elif choice == "7":
            gallery_id = input("Enter Gallery ID: ")
            artwork_id = input("Enter Artwork ID: ")
            gallery_service.add_artwork_to_gallery(gallery_id, artwork_id)

        elif choice == "8":
            gallery_id = input("Enter Gallery ID: ")
            artwork_id = input("Enter Artwork ID: ")
            gallery_service.remove_artwork_from_gallery(gallery_id, artwork_id)

        elif choice == "9":
            gallery_id = input("Enter Gallery ID: ")
            artworks = gallery_service.get_gallery_artworks(gallery_id)
            if artworks and len(artworks) > 0:
                print("\n🖼 Artworks in Your Gallery:")
                for art in artworks:
                    if len(art) >= 3:
                        print(f"ID: {art[0]}, Title: {art[1]}, Medium: {art[2]}")
                    else:
                        print(f"⚠ Invalid data format: {art}")
            else:
                print("⚠ No artworks found in this gallery.")

        elif choice == "10":
            gallery_id = input("Enter Gallery ID: ")
            gallery_service.delete_user_gallery(gallery_id)

        elif choice == "11":
            artwork_id = input("Enter Artwork ID to update: ")
            title = input("Enter new title: ")
            artist_id = input("Enter new artist ID: ")
            category_id = input("Enter new category ID: ")
            creation_date = input("Enter new creation date (YYYY-MM-DD): ")
            medium = input("Enter new medium: ")
            image_url = input("Enter new image URL: ")
            artwork = Artwork(artwork_id, title, artist_id, category_id, creation_date, medium, image_url)
            gallery_service.update_artwork(artwork)

        elif choice == "12":
            keyword = input("Enter keyword to search artworks: ")
            artworks = gallery_service.search_artworks(keyword)
            if artworks:
                print("\n Matching Artworks:")
                for art in artworks:
                    print(f"ID: {art[0]}, Title: {art[1]}, Medium: {art[2]}")
            else:
                print("❌ No artworks found matching the keyword.")

        elif choice == "13":
            artists = gallery_service.get_all_artists()
            if artists:
                print("\n All Artists:")
                for artist in artists:
                    print(f"ID: {artist[0]}, Name: {artist[1]}")
            else:
                print("❌ No artists found.")

        elif choice == "14":
            categories = gallery_service.get_all_categories()
            if categories:
                print("\n All Categories:")
                for category in categories:
                    print(f"ID: {category[0]}, Name: {category[1]}")
            else:
                print("❌ No categories found.")

        elif choice == "15":
            print(" Exiting... Thank you for using Virtual Art Gallery System!")
            break

        else:
            print("❌ Invalid choice! Please enter a valid option (1-15).")

if __name__ == "__main__":
    main()
