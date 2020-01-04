def evaluate_num_of_search_result(is_search_recursive, total_url_qt):
    """To provide min search results if search is not recursive. Yandex limits is 50 urls so it was set as a max.
    @return: int num_per_page
    """
    num_per_page = 20 if is_search_recursive else total_url_qt
    if total_url_qt > 51:
        num_per_page = 50
    return num_per_page


def create_yandex_url(search_site, num_per_page, search_query):
    """ Create search url for yandex by patten.
    @return: str search_url
    """
    search_url = f"{search_site}/search/?text={search_query}&numdoc={num_per_page}"
    return search_url


def create_google_url(search_site, num_per_page, search_query):
    """Create search url for google by patten.
    @return: str search_url
     """
    search_url = f"{search_site}/search?num={num_per_page}&q={search_query}"
    return search_url


def url_creator(search_site, is_search_recursive, total_url_qt, search_query):
    """Main func to evaluate user input and choose for what search engine create a url
    @return: str url
    """
    num_per_page = evaluate_num_of_search_result(is_search_recursive, total_url_qt)
    if "yandex" in search_site:
        search_url = create_yandex_url(search_site, num_per_page, search_query)
    else:
        search_url = create_google_url(search_site, num_per_page, search_query)
    print("Ссылка для поиска", search_url)
    return search_url
