from langdetect import detect
from logs import logging


def checking_for_blank_input(test_parameter):
    """Checking if user's input is blank.
    @return: user's input as a str or error message to console and empty str "" if user input was blank.
    """
    if not test_parameter:
        print("Please check your input data. It is blank! \n")
        test_parameter = ''
    return test_parameter


def get_valid_search_site(search_site):
    """Checks if user's chosen site is google.com or yandex.ru.
    @return: a str with valid url "https://www.yandex.ru", "https://www.google.com" or str "" if input data does not
    match up.
    """
    if "ya" in search_site.lower():
        search_site = "https://www.yandex.ru"
    elif "google" in search_site.lower():
        search_site = "https://www.google.com"
    else:
        print("We can search yandex.ru and google.com ONLY")
        search_site = ""
    return search_site


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
        search_site = get_valid_search_site(search_site)
        language = is_query_in_russian(search_query)
        if "google" in search_site and language:
            print("We can search russian language query only via yandex.ru \n"
                  "Search engine has been changed to yandex.ru")
            search_site = ""
    return search_site


def input_is_recursive():
    """Ask for user choice for recursive choice, checks for blank input. In case of incorrect input data this func
    will continuously ask for input.
    @return: True for recursive search and False for not-recursive
    """
    is_search_recursive = None
    while is_search_recursive == None:
        is_search_recursive = input("Please type 1 if you want to use recursive search and 0 if not:\n").strip()
        is_search_recursive = checking_for_blank_input(is_search_recursive)
        try:
            is_search_recursive = bool(int(is_search_recursive))
        except ValueError:
            logging.exception(f"ValueError in is_search_recursive. User has entered {is_search_recursive}")
            print("Please enter a number! 1 - for recursive and 0 - for not")
            is_search_recursive = None
    return is_search_recursive


def input_qt_url_to_find():
    """Ask for user choice for quantity of search results. Checks for blank input or if user input 0. In case of
    incorrect input data this func will continuously ask for input.
    @return: total_url_qt as int
    """
    total_url_qt = 0
    while not total_url_qt:
        try:
            total_url_qt = int(input("How many search results do you want? Please type in a integer from 10 up to "
                                     "50:\n").strip())
            if total_url_qt <= 0:
                print("You have entered a 0 or negative number. \n Please try again")
                total_url_qt = 0
        except ValueError:
            logging.exception(f"ValueError in input_qt_url_to_find.")
            print("Please enter a integer")
    return total_url_qt


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
    search_query, search_site, is_search_recursive, total_url_qt = input_user_data()
    print(search_query, search_site, is_search_recursive, total_url_qt)
