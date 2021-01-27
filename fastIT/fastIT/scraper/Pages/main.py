from scraper.PageModels.remote_fetching import *
from scraper.PageModels.api_fetching import *
from scraper.Selectors import page_selectors, apiSelectors
from scraper.Database.database import *

"""
One website -> one class definition
-> All classes inherit from either manual or remote fetch [manual:selenium, remote:requests]
-> fetching_data method triggers main mechanism to scrap web (each web has different structure)
"""

class Model:
    def __init__(self, base_link, web, type=None):
        self.base_link = base_link
        self.web = web
        self.db = Database(self.web)
        self.first_item_on_the_list = self.db.get_first_available_link()
        self.type = type
        self.scraping_instance = None
        if self.type == "api":
            self.selector = getattr(apiSelectors, self.web)
            self.scraping_instance = ApiFetching(link=self.base_link,
                                   web=self.web,
                                   selector=self.selector,
                                   first_db_link = self.first_item_on_the_list
                                   )
        elif self.type == "scraper":
            self.selector = getattr(page_selectors, self.web)
            self.scraping_instance = RemoteScraper(web=self.web,
                                        base_link=self.base_link,
                                        first_db_link = self.first_item_on_the_list,
                                        selector=self.selector
                                        )
        else:
            raise AttributeError("Only two types available - Api or scraper. Provided: "+str(type))

    def fetch_data(self):
        input_data = None
        if isinstance(self.scraping_instance, ApiFetching):
            input_data = self.scraping_instance.retrieve_data()
        elif isinstance(self.scraping_instance, RemoteScraper):
            self.scraping_instance.trigger()
            input_data = self.scraping_instance.data
        self.db.add_new_links(input=input_data)
        return input_data

