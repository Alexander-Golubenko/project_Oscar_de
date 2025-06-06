

def choose_language() -> str:
    """
    Prompts the user to select the interface language.
    """
    print("\nВыберите язык / Sprache wählen:")
    print("1. Русский")
    print("2. Deutsch")
    while True:
        lang_choice = input("\nВведите номер языка (1 или 2) \n/ Geben Sie die Nummer der Sprache ein (1 oder 2): ").strip()
        if lang_choice == "1":
            return "ru"
        elif lang_choice == "2":
            return "de"
        else:
            print("Неверный выбор / Ungültige Auswahl")


translations = {
    "ru": {
        "menu_title": "--- Меню ---",
        "menu_option_1": "1. Поиск по ключевому слову",
        "menu_option_2": "2. Поиск по жанру и году",
        "menu_option_3": "3. Показать популярные запросы",
        "menu_option_0": "0. Завершить программу",
        "menu_prompt": "Выберите один из вариантов ( 1 / 2 / 3 / 0 ): ",
        "keyword_prompt": "Введите ключевое слово для поиска фильмов: ",
        "no_results": "По вашему запросу ничего не найдено.",
        "continue_prompt": "Сделать ещё один запрос? (Y/N): ",
        "invalid_choice": "Неверный выбор. Попробуйте снова.",
        "empty_input": "Пустой ввод. Попробуйте снова.",
        "exit_message": "Завершение работы.",
        "popular_queries_title": "Популярные поисковые запросы:",
        "no_query_records": "Нет записей поисковых запросов.",
        "enter_film_number": "Введите номер фильма для подробностей или нажмите Enter для пропуска: ",
        "invalid_film_number": "Неверный номер фильма. Попробуйте ещё раз.",
        "genre_prompt": "Выберите номер жанра или нажмите Enter для любого жанра: ",
        "invalid_genre_number": "Неверный номер жанра. Попробуйте ещё раз.",
        "year_prompt": "Введите год выпуска или нажмите Enter для любого года: ",
        "invalid_year": "Ошибка ввода. Введите корректный год или Enter для пропуска.",
        "year_out_of_range": "Год вне допустимого диапазона. Попробуйте ещё раз.",
        "available_genres": "Доступные жанры:",
        "year_range": "Допустимый диапазон лет: {min_year} – {max_year}",
        "film_not_found": "Фильм не найден.",
        "next_page": "следующая страница",
        "return_to_menu": "выйти в меню",
        "film_labels": [
            "Название фильма", "Описание", "Год",
            "Длительность, мин", "Язык", "Актёры", "Жанры"
        ],
        "times_suffix": "раз(а)",
    },
    "de": {
        "menu_title": "--- Menü ---",
        "menu_option_1": "1. Suche nach Schlüsselwort",
        "menu_option_2": "2. Suche nach Genre und Jahr",
        "menu_option_3": "3. Beliebte Suchanfragen anzeigen",
        "menu_option_0": "0. Programm beenden",
        "menu_prompt": "Wählen Sie eine Option (1 / 2 / 3 / 0): ",
        "keyword_prompt": "Geben Sie ein Schlüsselwort für die Filmsuche ein: ",
        "no_results": "Keine Ergebnisse für Ihre Anfrage gefunden.",
        "continue_prompt": "Möchten Sie eine weitere Suche durchführen? (Y/N): ",
        "invalid_choice": "Ungültige Auswahl. Bitte versuchen Sie es erneut.",
        "empty_input": "Leere Eingabe. Bitte versuchen Sie es erneut.",
        "exit_message": "Programm wird beendet.",
        "popular_queries_title": "Beliebte Suchanfragen:",
        "no_query_records": "Keine Suchanfragen vorhanden.",
        "enter_film_number": "Geben Sie die Filmnummer ein oder drücken Sie Enter zum Überspringen: ",
        "invalid_film_number": "Ungültige Filmnummer. Bitte versuchen Sie es erneut.",
        "genre_prompt": "Wählen Sie eine Genre-Nummer oder drücken Sie Enter für alle Genres: ",
        "invalid_genre_number": "Ungültige Genre-Nummer. Bitte versuchen Sie es erneut.",
        "year_prompt": "Geben Sie das Erscheinungsjahr ein oder drücken Sie Enter für alle Jahre: ",
        "invalid_year": "Ungültige Eingabe. Bitte geben Sie ein gültiges Jahr oder Enter ein.",
        "year_out_of_range": "Jahr außerhalb des gültigen Bereichs. Bitte versuchen Sie es erneut.",
        "available_genres": "Verfügbare Genres:",
        "year_range": "Gültiger Jahresbereich: {min_year} – {max_year}",
        "film_not_found": "Film nicht gefunden.",
        "next_page": "nächste Seite",
        "return_to_menu": "zurück zum Menü",
        "film_labels": [
            "Filmtitel", "Beschreibung", "Jahr",
            "Dauer (Min.)", "Sprache", "Schauspieler", "Genres"
        ],
        "times_suffix": "mal",
    }
}


def get_translator(lang: str) -> dict:
    return translations.get(lang, translations["ru"])