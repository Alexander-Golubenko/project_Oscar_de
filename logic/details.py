from project_Oscar_de.db.connector import get_connection
from project_Oscar_de.logic.logger import log_error
from project_Oscar_de.db.queries import GET_FILM_DETAILS
from tabulate import tabulate
import textwrap


def get_film_details(film_id: int, t: dict) -> None:
    """
    Выводит карточку фильма с использованием переведённых названий полей.

    :param film_id: ID фильма для отображения
    :param t: Словарь перевода текущего языка
    """
    conn = get_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cursor:
            cursor.execute(GET_FILM_DETAILS, (film_id,))
            result = cursor.fetchone()

        if result:
            result = list(result)

            # Перенос длинных строк
            result[1] = textwrap.fill(result[1], width=80)  # Описание
            result[5] = textwrap.fill(result[5], width=80)  # Актёры
            result[6] = textwrap.fill(result[6], width=80)  # Жанры

            labels = t["film_labels"]
            table = list(zip(labels, result))
            print("\n" + tabulate(table, tablefmt="grid"))
        else:
            print(t["film_not_found"])

    except Exception as e:
        log_error("get_film_details", e)
        print(f"Error while retrieving film details: {e}")

    finally:
        conn.close()