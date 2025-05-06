from project_Oscar_de.logic.search import search_by_keyword, search_by_genre_and_year
from project_Oscar_de.logic.analytics import get_popular_searches
from project_Oscar_de.ui.console import (
    show_menu,
    ask_keyword,
    ask_genre_and_year,
    show_search_results,
    show_popular_queries,
    ask_continue
)
from project_Oscar_de.logic.details import get_film_details
from project_Oscar_de.ui.local import get_translator


def choose_language() -> str:
    """
    Предлагает пользователю выбрать язык интерфейса.
    """
    print("Choose language / Выберите язык:")
    print("1. Русский")
    print("2. Deutsch")
    while True:
        lang_choice = input("Введите номер языка (1 или 2): ").strip()
        if lang_choice == "1":
            return "ru"
        elif lang_choice == "2":
            return "de"
        else:
            print("Неверный выбор / Ungültige Auswahl")


def main() -> None:
    """
    Основная точка входа программы. Отображает меню и обрабатывает пользовательские команды.
    """
    lang = choose_language()
    t = get_translator(lang)

    while True:
        choice = show_menu(t)

        if choice == "0":
            print(t["exit_message"])
            break

        elif choice == "1":
            keyword = ask_keyword(t)
            if not keyword:
                print(t["empty_input"])
                continue
            results = search_by_keyword(keyword)
            film_id = show_search_results(results, t)
            if film_id:
                get_film_details(film_id, t)

        elif choice == "2":
            genre_year = ask_genre_and_year(t)
            if genre_year is None:
                continue
            genre, year = genre_year
            results = search_by_genre_and_year(genre, year)
            if not results:
                print("\n" + t["no_results"])
            else:
                film_id = show_search_results(results, t, show_year=False)
                if film_id:
                    get_film_details(film_id, t)

        elif choice == "3":
            queries = get_popular_searches()
            show_popular_queries(queries, t)

        else:
            print(t["invalid_choice"])

        if not ask_continue(t):
            print(t["exit_message"])
            break


if __name__ == "__main__":
    main()