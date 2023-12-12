import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_book_len_more_40_symbols_is_None(self):
        #создаем объект класса collector
        collector = BooksCollector()
        #добавляем книгу с названием больше 40 символов
        collector.add_new_book('Очень длинное название книги, которое превышает 40 символов')

        #проверяем что книга больше 40 символов не включена в список
        assert collector.books_genre.get('Очень длинное название книги, которое превышает 40 символов') is None

    def test_add_new_book_add_book_len_0_is_None(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert collector.books_genre.get('') is None

    def test_set_book_genre_have_set(self):
        collector = BooksCollector()
        collector.add_new_book("Как улучшить тренажер? Пошаговое пособие")
        collector.set_book_genre("Как улучшить тренажер? Пошаговое пособие", "Комедии")
        collector.get_book_genre("Как улучшить тренажер? Пошаговое пособие")
        assert collector.get_book_genre("Как улучшить тренажер? Пошаговое пособие") == "Комедии"

    def test_get_books_with_specific_genre_have_got_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book")
        collector.set_book_genre("Book", "Ужасы")

        assert collector.get_books_with_specific_genre("Ужасы") == ["Book"]

    def test_get_books_genre_have_got_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Book")
        collector.set_book_genre("Book", "Ужасы")

        assert collector.get_books_genre() == {'Book': 'Ужасы'}

    def test_get_books_for_children_have_got_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("BookForChildren")
        collector.set_book_genre("BookForChildren", "Мультфильмы")

        assert collector.get_books_for_children() == ["BookForChildren"]

    def test_add_book_in_favorites_book_added(self):
        collector = BooksCollector()
        collector.add_new_book("FavoriteBook")
        collector.add_book_in_favorites("FavoriteBook")

        assert collector.get_list_of_favorites_books() == ["FavoriteBook"]

    def test_delete_book_from_favorites_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book("FavoriteBook")
        collector.add_book_in_favorites("FavoriteBook")
        collector.delete_book_from_favorites("FavoriteBook")

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_have_got_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("FavoriteBook")
        collector.add_book_in_favorites("FavoriteBook")

        assert collector.get_list_of_favorites_books() == ["FavoriteBook"]

    @pytest.mark.parametrize('book', ['Book1', 'Book2', 'Book3'])
    def test_get_book_genre_have_got_book_genre(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, "Комедии")
        assert collector.get_book_genre(book) == "Комедии"