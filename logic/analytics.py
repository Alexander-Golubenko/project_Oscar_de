from project_Oscar_de.db.connector import get_log_connection
from project_Oscar_de.db.queries import POPULAR_SEARCHES
from project_Oscar_de.logic.logger import log_error
from typing import List, Tuple


def get_popular_searches(limit: int = 10) -> List[Tuple[str, int]]:
    """
    Возвращает список самых популярных поисковых запросов.

    :param limit: Количество запросов
    :return: Список кортежей (запрос, количество)
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
        print(f"Ошибка при получении популярных запросов: {e}")
        return []
    finally:
        conn.close()