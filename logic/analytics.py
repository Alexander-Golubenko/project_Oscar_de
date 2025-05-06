from project_Oscar_de.db.connector import get_log_connection
from project_Oscar_de.db.queries import POPULAR_SEARCHES
from project_Oscar_de.logic.logger import log_error
from typing import List, Tuple
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_popular_searches(limit: int = 10) -> List[Tuple[str, int]]:
    """
    Returns a list of the most popular search queries.

    :param limit: Number of queries to return
    :return: List of tuples (query, count)
    """
    conn = get_log_connection()
    if conn is None:
        return []
    try:
        with conn.cursor() as cursor:
            cursor.execute(POPULAR_SEARCHES, (limit,))
            results = cursor.fetchall()
        return results
    except Exception as e:
        log_error("get_popular_searches", e)
        clear_screen()
        print(f"Error while retrieving popular searches: {e}")
        return []
    finally:
        conn.close()