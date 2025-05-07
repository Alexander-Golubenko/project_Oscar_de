from project_Oscar_de.logic.details import get_film_details
from project_Oscar_de.logic.search import get_all_genres, get_year_range
from typing import List, Tuple
import os

def clear_screen():
    """
    Clears the terminal screen (cross-platform).
    """
    os.system("cls" if os.name == "nt" else "clear")

def show_menu(t: dict) -> str:
    """
    Displays the main menu and returns the user's choice.
    """
    clear_screen()
    print(f"\n{t['menu_title']}")
    print(t["menu_option_1"])
    print(t["menu_option_2"])
    print(t["menu_option_3"])
    print(t["menu_option_0"])
    return input(t["menu_prompt"]).strip()


def ask_keyword(t: dict) -> str:
    """
    Prompts the user to enter a keyword for the search.
    """
    clear_screen()
    return input(t["keyword_prompt"]).strip()


def ask_genre_and_year(t: dict) -> Tuple[str | None, int | None] | None:
    """
    Prompts the user to select a genre (or press Enter for any) and a release year (or press Enter for any).
    """
    genres = get_all_genres()
    if not genres:
        clear_screen()
        print(t["no_results"])
        return None

    clear_screen()
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
        clear_screen()
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

def paginate(items: List[Tuple], size: int = 20):
    """
    Generator that yields chunks of a list with a given page size.
    """
    for i in range(0, len(items), size):
        yield items[i:i + size]

def show_search_results(results: List[Tuple], t: dict, show_year: bool = True) -> int | None:
    """
    Displays movies in pages and allows user to select one, go to next page, or exit.
    """
    if not results:
        print("\n" + t["no_results"])
        return None

    start_index = 0

    for page in paginate(results):
        clear_screen()

        for i, film in enumerate(page, start=start_index + 1):
            if len(film) >= 3:
                title = f"{film[1]} ({film[2]})" if show_year else film[1]
            else:
                title = film[1] if len(film) > 1 else str(film)
            print(f"{i}. {title}")

        has_next_page = start_index + len(page) < len(results)

        prompt = f"\n{t['enter_film_number']}"
        if has_next_page:
            prompt += f" [n = {t.get('next_page', 'next')}]"

        user_input = input(prompt).strip().lower()

        if user_input == "":
            return None
        if user_input == "n":
            start_index += len(page)
            continue
        if user_input.isdigit():
            index = int(user_input) - 1
            return results[index][0] if 0 <= index < len(results) else None

        print(t["invalid_film_number"])
        return None

    return None


def ask_continue(t: dict) -> bool:
    """
    Asks the user whether they want to continue using the application.
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
    Displays a list of popular queries along with their frequencies.
    """
    if queries:
        clear_screen()
        print(f"\n{t['popular_queries_title']}")
        for i, (term, freq) in enumerate(queries, start=1):
            print(f"{i}. {term} — {freq} {t['times_suffix']}")
    else:
        clear_screen()
        print(t["no_query_records"])

