from scraper.Imports import requests

class ApiFetching():
    def __init__(self, link=None, web=None, selector=None, first_db_link=None):
        self.web = web
        self.link = link
        self.selector = selector
        self.first_db_link = first_db_link
        print(f"Fetching {self.web}")

    def _retrieve_content(self):
        return requests.get(self.selector.api_link).json()

    def _set_variables(self, iterator: dict):
        for globalVar in (self.selector.url, self.selector.title, self.selector.city):
            var = None
            if self.web == "nofluffjobs" and globalVar == self.selector.city:
                var = iterator["location"]["places"][0][self.selector.city]
            else:
                var = iterator[globalVar]
            yield var

    def retrieve_data(self):
        raw_data = self._retrieve_content()
        if len(self.selector.parent) > 0:
            raw_data = raw_data[self.selector.parent]
        for single in raw_data:
            try:
                link, title, city = self._set_variables(single)
                if self.first_db_link != None and self.first_db_link in self.link+link:
                    print(f"{self.web}, Found the first element from previous iteration: Stopping")
                    break
                yield self.link+link, title, city
            except Exception as e:
                raise Exception(f"Issue occured while fetching data from, {self.link} "+str(e))
