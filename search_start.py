from bs4 import BeautifulSoup
import requests

from data_input import input_user_data
from url_create import url_creator


def get_html(search_url):
    """Opens a search_url and returns a response object text
    """
    try:
        result = requests.get(search_url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print("Net Error")
        return False


def search_sites_by_google(result_html):
    """Looking for urls with search results only. Create a BS object and looks for all <div> tags in HTML with class
    "kCrYT", selects only external links with https. Also cleans found urls from google prefix and /url?=q
    @return: list of found urls
    """
    soup_results = BeautifulSoup(result_html, "html.parser")
    html_found = soup_results.find_all("div", class_="kCrYT")
    list_urls_found = []
    for site in html_found:
        a_tag_found = site.find('a')
        if a_tag_found:
            url_found = a_tag_found['href']
            if "http" in url_found:
                url = url_found.partition("&")[0]
                url_cleaned = url.strip("/url?=q")
                list_urls_found.append(url_cleaned)
    print(list_urls_found)
    return list(set(list_urls_found))


def search_sites_yandex(result_html):
    """Looking for urls with search results only. Create a BS object and looks for all <a> tags in HTML with
    attribute tabindex=2, selects only external links with https.
    @return: list of found urls
    """
    soup_results = BeautifulSoup(result_html, "html.parser")
    list_of_finded_sites = soup_results.find_all("a", tabindex=2)
    list_urls = []
    for site in list_of_finded_sites:
        if "https" in site["href"]:
            list_urls.append(site["href"])
    return list_urls


def recursive_search(url, total_url_qt):
    """While qt of urls found less than User asked for open every ling from step above. Create a BS object and looks
    for all <a> tags in HTML, selects only external links with https. Adds found urls to list
    @return: list of found urls
    """
    search_result = url[:]
    print("Запускаю рекрусивный поиск")
    for i in url:
        while len(search_result) < total_url_qt:
            result_html = get_html(i)
            print("Готово")
            if result_html:
                soup_results = BeautifulSoup(result_html, "html.parser")
                list_of_found_urls = soup_results.find_all("a", href=True)
                for url in list_of_found_urls:
                    if "https" in url["href"]:
                        search_result.append(url["href"])
    return search_result


def print_search_result(total_url_qt, found_url_list):
    """Cuts the qt of found urls to total_url_qt and prints them in console with number.
    """
    if len(found_url_list) > total_url_qt:
        found_url_list = found_url_list[:total_url_qt]
    print(f"We have found: {len(found_url_list)} links")
    for index, link in enumerate(found_url_list, start=1):
        print(f"{index}: {link}")


def url_search_launch():
    """This is a console search engine. User inputs search query, whether use yandex.ru or google.com, total qt of
    search results, whether use recursive search or not. Current version deals with 1 word query in english (for
    google.com) and both eng and ru for yandex.ru. Total qt of search results are limited by 50.
    """
    search_query, search_site, is_search_recursive, total_url_qt = input_user_data()
    search_url = url_creator(search_site, is_search_recursive, total_url_qt, search_query)
    result_html = get_html(search_url)
    if not result_html:
        print("Search is temporary unvailable. Sorry! Please try again later")
        return None
    if "yandex" in search_url:
        found_url_list = search_sites_yandex(result_html)
    elif "google" in search_url:
        found_url_list = search_sites_by_google(result_html)
    if is_search_recursive:
        found_url_list = recursive_search(found_url_list, total_url_qt)
    print_search_result(total_url_qt, found_url_list)


if __name__ == "__main__":
    url_search_launch()
