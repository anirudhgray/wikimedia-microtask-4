import validators


def validate_url(url):
    """
    Heuristic:
    - No google/bing/ddg/etc search results.
    - No wikipedia article pages.
    - A list of blocked untrustworthy publications (maybe).
    """

    error = None
    if not validators.url(url):
        error = "URL malformed."
        return error

    SEARCH_ENGINES = ['https://www.google.com/search?q=',
                      'https://duckduckgo.com/?q=', 'https://www.bing.com/search?q=']
    for i in SEARCH_ENGINES:
        if url.startswith(i):
            error = "Search engine results not allowed!"

    UNTRUSTWORTHY = []
    for i in UNTRUSTWORTHY:
        if url.startswith(i):
            error = "Untrustworthy source!"

    WIKIPEDIA_EXCLUDE = ['https://en.wikipedia.org/wiki/Help:',
                         'https://en.wikipedia.org/wiki/Wikipedia:']
    if url.startswith('https://en.wikipedia.org/wiki/'):
        flag = True
        for i in WIKIPEDIA_EXCLUDE:
            if url.startswith(i):
                flag = False
        if flag:
            error = "Wikipedia articles not allowed!"

    return error
