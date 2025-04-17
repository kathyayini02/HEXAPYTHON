import pytest
from unittest.mock import MagicMock, patch
from dao.virtualartgalleryimpl import VirtualArtGalleryImpl
from entity.artwork import Artwork

@pytest.fixture
def gallery():
    with patch('dao.virtualartgalleryimpl.DBConnection.get_connection') as mock_conn:
        mock = MagicMock()
        mock_conn.return_value = mock
        return VirtualArtGalleryImpl()

def test_add_artwork_success(gallery):
    mock_cursor = gallery.conn.cursor.return_value
    artwork = Artwork(1, "Mona Lisa", 1, 1, "1503-06-01", "Oil", "url")
    gallery.add_artwork(artwork)
    assert mock_cursor.execute.called

def test_get_artwork_by_id_found(gallery):
    mock_cursor = gallery.conn.cursor.return_value
    mock_cursor.fetchone.return_value = ("Mona Lisa",)
    result = gallery.get_artwork_by_id(1)
    assert result == ("Mona Lisa",)

def test_get_artwork_by_id_not_found(gallery):
    mock_cursor = gallery.conn.cursor.return_value
    mock_cursor.fetchone.return_value = None
    result = gallery.get_artwork_by_id(99)
    assert "❌ No artwork found" in result

def test_remove_artwork_not_found(gallery, capsys):
    mock_cursor = gallery.conn.cursor.return_value
    mock_cursor.fetchone.return_value = [0]
    gallery.remove_artwork(99)
    captured = capsys.readouterr()
    assert "does not exist" in captured.out

def test_update_artwork_success(gallery):
    mock_cursor = gallery.conn.cursor.return_value
    artwork = Artwork(1, "Updated Title", 2, 2, "2020-01-01", "Watercolor", "new_url")
    gallery.update_artwork(artwork)
    assert mock_cursor.execute.called

def test_search_artworks_found(gallery):
    mock_cursor = gallery.conn.cursor.return_value
    mock_cursor.fetchall.return_value = [("Sunset",)]
    result = gallery.search_artworks("Sun")
    assert isinstance(result, list)

def test_search_artworks_not_found(gallery):
    mock_cursor = gallery.conn.cursor.return_value
    mock_cursor.fetchall.return_value = []
    result = gallery.search_artworks("Unknown")
    assert "❌ No artworks found" in result

def test_get_all_artworks_empty(gallery):
    gallery.conn.cursor.return_value.fetchall.return_value = []
    result = gallery.get_all_artworks()
    assert "❌ No artworks found." in result

def test_get_all_artists_success(gallery):
    gallery.conn.cursor.return_value.fetchall.return_value = [("Da Vinci",)]
    result = gallery.get_all_artists()
    assert result[0][0] == "Da Vinci"

def test_create_user_gallery_success(gallery):
    gallery.create_user_gallery(1, "My Gallery", "Cool art")
    assert gallery.conn.cursor.return_value.execute.called

def test_get_user_galleries_none(gallery):
    gallery.conn.cursor.return_value.fetchall.return_value = []
    result = gallery.get_user_galleries(42)
    assert "❌ No galleries found" in result

def test_add_artwork_to_gallery(gallery):
    gallery.add_artwork_to_gallery(1, 1)
    assert gallery.conn.cursor.return_value.execute.called

def test_remove_artwork_from_gallery(gallery):
    gallery.remove_artwork_from_gallery(1, 1)
    assert gallery.conn.cursor.return_value.execute.called

def test_get_gallery_artworks_none(gallery):
    gallery.conn.cursor.return_value.fetchall.return_value = []
    result = gallery.get_gallery_artworks(1)
    assert "❌ No artworks found" in result

def test_delete_user_gallery_success(gallery):
    gallery.delete_user_gallery(1)
    assert gallery.conn.cursor.return_value.execute.call_count == 2