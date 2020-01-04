from data_input import input_user_data
from search import get_html, search_exeсute, print_search_result
from url_create import url_creator


def url_search_launch():
    """This is a console search engine. User inputs search query, whether use yandex.ru or google.com, total qt of
    search results, whether use recursive search or not. Current version deals with 1 word query in english (for
    google.com) and both eng and ru for yandex.ru. Total qt of search results are limited by 50.
    """
    search_query, search_site, is_search_recursive, total_url_qt = input_user_data()
    search_url = url_creator(search_site, is_search_recursive, total_url_qt, search_query)
    result_html = get_html(search_url)
    found_url_list = search_exeсute(result_html, search_url, is_search_recursive, total_url_qt)
    if found_url_list:
        print_search_result(total_url_qt, found_url_list)


if __name__ == "__main__":
    url_search_launch()
