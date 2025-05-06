from project_Oscar_de.logic.details import get_film_details
from project_Oscar_de.logic.search import get_all_genres, get_year_range
from typing import List, Tuple


def show_menu(t: dict) -> str:
    """
    Отображает главное меню и возвращает выбор пользователя.
    """
    print(f"\n{t['menu_title']}")
    print(t["menu_option_1"])
    print(t["menu_option_2"])
    print(t["menu_option_3"])
    print(t["menu_option_0"])
    return input(t["menu_prompt"]).strip()


def ask_keyword(t: dict) -> str:
    """
    Запрашивает у пользователя ключевое слово для поиска.
    """
    return input(t["keyword_prompt"]).strip()


def ask_genre_and_year(t: dict) -> Tuple[str | None, int | None] | None:
    """
    Запрашивает у пользователя жанр (или Enter для любого) и год выпуска (или Enter для любого).
    """
    genres = get_all_genres()
    if not genres:
        print(t["no_results"])
        return None

    print(f"\n{t['available_genres']}")
    for i, genre in enumerate(genres, start=1):
        print(f"{i}. {genre}")

    selected_genre = None
    while True:
        genre_input = input(t["genre_prompt"]).strip()
        if genre_input == "":
            selected_genre = None
            break
        if genre_input.isdigit():
            genre_choice = int(genre_input)
            if 1 <= genre_choice <= len(genres):
                selected_genre = genres[genre_choice - 1]
                break
            else:
                print(t["invalid_genre_number"])
        else:
            print(t["invalid_genre_number"])

    year_range = get_year_range(selected_genre)
    if not year_range:
        print(t["no_results"])
        return None

    min_year, max_year = year_range
    print(t["year_range"].format(min_year=min_year, max_year=max_year))

    selected_year = None
    while True:
        year_input = input(t["year_prompt"]).strip()
        if year_input == "":
            selected_year = None
            break
        if year_input.isdigit():
            year = int(year_input)
            if min_year <= year <= max_year:
                selected_year = year
                break
            else:
                print(t["year_out_of_range"])
        else:
            print(t["invalid_year"])

    return selected_genre, selected_year


def show_search_results(results: List[Tuple], t: dict, show_year: bool = True) -> int | None:
    """
    Отображает список фильмов и предлагает выбрать один для просмотра деталей.
    """
    if not results:
        print("\n" + t["no_results"])
        return None

    while True:
        print("\n" + t["menu_option_1"])  # название блока (например, "Найденные фильмы")
        for i, item in enumerate(results, start=1):
            title = f"{item[1]} ({item[2]})" if show_year and len(item) > 2 else item[1]
            print(f"{i}. {title}")

        sub_choice = input(t["enter_film_number"]).strip()
        if sub_choice == "":
            return None

        if sub_choice.isdigit():
            index = int(sub_choice) - 1
            if 0 <= index < len(results):
                return results[index][0]
            else:
                print(t["invalid_film_number"])
        else:
            print(t["invalid_film_number"])


def ask_continue(t: dict) -> bool:
    """
    Спрашивает пользователя, хочет ли он продолжить работу с приложением.
    """
    while True:
        again = input(f"\n{t['continue_prompt']}").strip().lower()
        if again in ("y", "yes", "j", "ja"):
            return True
        elif again in ("n", "no", "nein"):
            return False
        else:
            print(t["invalid_choice"])


def show_popular_queries(queries: List[Tuple[str, int]], t: dict) -> None:
    """
    Отображает список популярных запросов с частотами.
    """
    if queries:
        print(f"\n{t['popular_queries_title']}")
        for i, (term, freq) in enumerate(queries, start=1):
            print(f"{i}. {term} — {freq} {t['times_suffix']}")
    else:
        print(t["no_query_records"])

