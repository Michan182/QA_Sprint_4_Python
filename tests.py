import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        """
         проверяем что добавилось 2 книги
        """
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    @pytest.mark.parametrize('book', ['',
                                      "Очень длинное название книги, которое пре",
                                      "Очень длинное название книги, которое прев"])
    def test_add_new_book_add_book_len_more_0_41_42_symbols_is_None(self, book):
        """
        проверяем что книги длиной 0,41,41 символов не добавились в словарь
        """
        collector = BooksCollector()
        collector.add_new_book(book)
        assert collector.get_book_genre(book) is None

    @pytest.mark.parametrize('book', ['B', 'Bo', "Очень длинное название книги, которое п","Очень длинное название книги, которое пр"])
    def test_add_new_book_add_book_len_1_2_39_40_symbols_is_added(self, book):
        """
        проверяем что книги длиной 1,2,39,40 символов добавились в словарь
        """
        collector = BooksCollector()
        collector.add_new_book(book)
        assert book in collector.get_books_genre().keys()

    def test_set_book_genre_have_set(self):
        """
        проверяем что у книги добавился жанр
        """
        collector = BooksCollector()
        collector.add_new_book("Как улучшить тренажер? Пошаговое пособие")
        collector.set_book_genre("Как улучшить тренажер? Пошаговое пособие", "Комедии")
        assert collector.get_book_genre("Как улучшить тренажер? Пошаговое пособие") == "Комедии"

    def test_get_books_with_specific_genre_have_got_books_with_specific_genre(self):
        """
        проверяем вывод книг с определенным жанром
        """
        collector = BooksCollector()
        collector.add_new_book("Book")
        collector.set_book_genre("Book", "Ужасы")
        collector.add_new_book("Book1")
        collector.set_book_genre("Book1", "Ужасы")
        collector.add_new_book("Book2")
        collector.set_book_genre("Book2", "Комедии")
        assert collector.get_books_with_specific_genre("Ужасы") == ["Book","Book1"]

    def test_get_books_genre_have_got_books_genre(self):
        """
        проверяем получение словаря с книгами и жанрами
        """
        collector = BooksCollector()
        collector.add_new_book("Book")
        collector.set_book_genre("Book", "Ужасы")

        assert collector.get_books_genre() == {'Book': 'Ужасы'}

    @pytest.mark.parametrize('book, genre', [
        ('BookForChildren', 'Мультфильмы'),
        ('BookForChildren1', 'Комедии'),
        ('BookForChildren2', 'Фантастика')]
                             )
    def test_get_books_for_children_have_got_books_for_children(self, book, genre):
        """
        Проверяем, что книги с разными жанрами возвращаются методом get_books_for_children
        """
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == [book]

    def test_add_book_in_favorites_book_added(self):
        """
        Проверяем, что книги добавлены в список избранных
        """
        collector = BooksCollector()
        collector.add_new_book("FavoriteBook")
        collector.add_book_in_favorites("FavoriteBook")

        assert collector.get_list_of_favorites_books() == ["FavoriteBook"]

    def test_delete_book_from_favorites_book_deleted(self):
        """
        Проверяем, что книги удалены из списка избранных
        """
        collector = BooksCollector()
        collector.add_new_book("FavoriteBook")
        collector.add_book_in_favorites("FavoriteBook")
        collector.delete_book_from_favorites("FavoriteBook")

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_have_got_list_of_favorites_books(self):
        """
        Проверяем, что список избранных книг возвращает нужное количество книг
        """
        collector = BooksCollector()
        collector.add_new_book("FavoriteBook")
        collector.add_book_in_favorites("FavoriteBook")

        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize('book, genre', [
        ('Book1', 'Ужасы'),
        ('Book2', 'Детективы'),
        ('Book3', 'Фантастика'),
    ])
    def test_get_book_genre_returns_expected_genre(self, book, genre):
        """
        Проверяем, что метод get_book_genre возвращает ожидаемый жанр для книги
        """
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre