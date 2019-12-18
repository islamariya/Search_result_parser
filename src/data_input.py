from langdetect import detect


def checking_for_blank_input(test_parameter):
    """Checking if user's input is blank.
    @return: user's input as a str or str "" if it is blank
    """
    if len(test_parameter) == 0:
        print("Please check your input data. It is blank! \n")
        test_parameter = ''
    return test_parameter


def is_site_ok(search_site):
    """Checks if user's chosen site is google.com or yandex.ru. It covers usege https, www and capital letters.
    @return: user's input as a str or str "" if input data does not match listed in site_possible
    """
    site_possible = ("http://www.google.com", "http://www.yandex.ru", "www.google.com",
                     "www.yandex.ru", "yandex.ru", "google.com")
    is_site_ok = search_site if search_site in site_possible else ""
    if not is_site_ok:
        print("We can search yandex.ru and google.com ONLY")
        is_site_ok = ""
    return is_site_ok


def is_query_in_russian(search_query):
    """Checking if the language of query is russian cause this version does not support google search for query in
    russian.
    @return: True if lang is russian and False if it is any other language
    """
    language = detect(search_query)
    is_russian = True if language == "ru" else False
    return is_russian


def input_search_query():
    """Ask for user choice for search query, checks for blank input. In case of incorrect input data this func will
    continuously ask for correct input.
    @return: user's input for search_query as a string
    """
    search_query = ""
    while not search_query:
        search_query = input("What is you looking for? Please type in your search query\n"
                             "Please be aware that we can only process query in russian via yandex.ru! \n").strip()
        search_query = checking_for_blank_input(search_query)
    return search_query


def input_search_engine(search_query):
    """Ask for user choice for search engine, checks for blank input, if it's yandex.ru or google.com. Also prevents
    queries in russian language for google.com. In case of incorrect input data this func will continuously ask for
    input.
    @return: user's input for search_site as a string
    """
    search_site = ""
    while not search_site:
        search_site = input("Please type in search engine: yandex.ru or google.com:\n").strip().lower()
        search_site = checking_for_blank_input(search_site)
        search_site = is_site_ok(search_site)
        language = is_query_in_russian(search_query)
        if "google" in search_site and language:
            print("We can search russian language query only via yandex.ru Please change search engine!")
            search_site = ""
    return search_site


def input_is_recursive():
    """Ask for user choice for recursive choice, checks for blank input. In case of incorrect input data this func
    will continuously ask for input.
    @return: True for recursive search and False for not-recursive
    """
    is_search_recursive = False
    while not is_search_recursive:
        is_search_recursive = input("Please type 1 if you want to use recursive search and 0 if not:\n").strip()
        is_search_recursive = checking_for_blank_input(is_search_recursive)
    return bool(int(is_search_recursive))


def input_qt_url_to_find():
    """Ask for user choice for quantity of search results. Checks for blank input or if user input 0. In case of
    incorrect input data this func will continuously ask for input.
    @return: total_url_qt as int
    """
    total_url_qt = 0
    while not total_url_qt:
        total_url_qt = input(
            "How many search results do you want? Please type in a integer from 10 up to 50:\n").strip()
        total_url_qt = checking_for_blank_input(total_url_qt)
        if total_url_qt == "0":
            print("You have entered a ZERO search results. Please try again)\n")
            total_url_qt = 0
    return int(total_url_qt)


def input_user_data():
    """Collects user data to start search.
    search_query: str in English or Russian, spaces at the beginning and end of string are deleted
    search_site: str might be yandex.ru or google.com
    is_search_recursive: bool. Deeps of recursive:1
    total_url_qt: int
    """
    print("To start the search please provide the information below!")
    print()
    search_query = input_search_query()
    search_site = input_search_engine(search_query)
    is_search_recursive = input_is_recursive()
    total_url_qt = input_qt_url_to_find()
    return search_query, search_site, is_search_recursive, total_url_qt


if __name__ == "__main__":
    input_user_data()
