"""ABC
"""
from classes.sitescrapper import Sitescrapper

site_scrapper = Sitescrapper('http://quotes.toscrape.com/')
site_scrapper.parse_pages()
