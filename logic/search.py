from project_Oscar_de.db.queries import (
    SEARCH_BY_KEYWORD,
    SEARCH_BY_GENRE_YEAR_BASE,
    CREATE_SEARCH_LOG_TABLE,
    INSERT_SEARCH_LOG,
    POPULAR_SEARCHES,
    GET_ALL_GENRES,
    GET_MIN_YEAR,
    GET_MAX_YEAR,
    GET_MIN_YEAR_BY_GENRE,
    GET_MAX_YEAR_BY_GENRE
)
from project_Oscar_de.db.connector import get_connection, get_log_connection
from project_Oscar_de.logic.logger import log_error
from typing import List, Tuple
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def search_by_keyword(keyword: str) -> List[Tuple[int, str, int]]:
    """
    Performs a movie search by keyword in the title.

    :param keyword: Search string
    :return: List of found movies (film_id, title, release_year)
    """
    results = []
    like_pattern = f"%{keyword}%"
    conn = get_connection()
    if conn is None:
        return results

    try:
        with conn.cursor() as cursor:
            cursor.execute(SEARCH_BY_KEYWORD, (like_pattern,))
            results = cursor.fetchall()

    except Exception as e:
        log_error("search_by_keyword", e)
        clear_screen()
        print(f"Error while executing search query: {e}")
    finally:
        conn.close()
    log_search("keyword", keyword)
    return results


def search_by_genre_and_year(genre: str | None, year: int | None) -> List[Tuple[int, str]]:
    """
    Performs a movie search by genre and/or release year.
    If genre or year is None, that filter is not applied.
    """
    results = []
    conn = get_connection()
    if conn is None:
        return results

    try:
        with conn.cursor() as cursor:

            query = SEARCH_BY_GENRE_YEAR_BASE
            conditions = []
            params = []

            if genre is not None:
                conditions.append("c.name = %s")
                params.append(genre)
            if year is not None:
                conditions.append("f.release_year = %s")
                params.append(year)

            if conditions:
                query += " WHERE " + " AND ".join(conditions)

            # query += " LIMIT 20;"

            cursor.execute(query, tuple(params))
            results = cursor.fetchall()

    except Exception as e:
        log_error("search_by_genre_and_year", e)
        clear_screen()
        print(f"Error while performing search by genre and year: {e}")
    finally:
        conn.close()

    # лог
    genre_text = genre if genre is not None else "any_genre"
    year_text = str(year) if year is not None else "any_year"
    log_search("genre_year", f"{genre_text}:{year_text}")

    return results


def log_search(search_type: str, query_text: str) -> None:
    """
    Logs the search query into the search_log table, tracking the count and the time of the last use.

    :param search_type: Type of the query (e.g., 'keyword', 'genre_year')
    :param query_text: The content of the query (what the user entered)
    """
    conn = get_log_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_SEARCH_LOG_TABLE)
            cursor.execute(INSERT_SEARCH_LOG, (search_type, query_text))
            conn.commit()
    except Exception as e:
        log_error("log_search", e)
        clear_screen()
        print(f"Error while logging the query: {e}")
    finally:
        conn.close()


def get_all_genres() -> List[str]:
    """
    Returns a list of all unique genres from the database, sorted alphabetically.
    """
    conn = get_connection()
    if conn is None:
        return []
    try:
        with conn.cursor() as cursor:
            cursor.execute(GET_ALL_GENRES)
            genres = [row[0] for row in cursor.fetchall()]
        return genres
    except Exception as e:
        log_error("get_all_genres", e)
        clear_screen()
        return []
    finally:
        conn.close()


def get_year_range(genre: str | None = None) -> Tuple[int, int] | None:
    """
    Returns the minimum and maximum release year of movies.
    If a genre is specified, the range is calculated only for movies of that genre.
    """
    conn = get_connection()
    if conn is None:
        return None
    try:
        with conn.cursor() as cursor:

            if genre:
                cursor.execute(GET_MIN_YEAR_BY_GENRE, (genre,))
                min_year = cursor.fetchone()[0]

                cursor.execute(GET_MAX_YEAR_BY_GENRE, (genre,))
                max_year = cursor.fetchone()[0]
            else:
                cursor.execute(GET_MIN_YEAR)
                min_year = cursor.fetchone()[0]

                cursor.execute(GET_MAX_YEAR)
                max_year = cursor.fetchone()[0]

        return min_year, max_year
    except Exception as e:
        log_error("get_year_range", e)
        clear_screen()
        return None
    finally:
        conn.close()

