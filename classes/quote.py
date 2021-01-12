"""ABC
"""
import requests
from bs4 import BeautifulSoup
from classes.author import Author


class Quote:
    """
    Attributes:
    text(string): the text of the quote
    tags(array of strings): list of tags
    author(Author): Author of the quote
    """

    def __init__(self, quote):
        for elmt in quote.contents:
            if elmt != '\n':
                if elmt.name == 'span':
                    if elmt.has_attr('class')\
                     and 'text' in elmt.attrs['class']:
                        self.text = elmt.string.replace("′", '\'')
                    elif elmt.small is not None:
                        self.author = Author(
                                        BeautifulSoup(
                                            requests.get(
                                                "http://quotes.toscrape.com"
                                                + elmt.a.get('href')
                                            ).content, 'lxml'
                                        )
                                      )

                if elmt.name == 'div':
                    self.tags = []
                    for child in elmt:
                        if child.name == 'a':
                            self.tags.append(child.string)
