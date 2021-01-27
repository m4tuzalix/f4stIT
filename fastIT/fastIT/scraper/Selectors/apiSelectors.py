class webSelectors():
    __slots__ = ["base_link", "api_link", "parent", "url", "title", "city", "kwargs"]
    def __init__(self, base_link, api_link,  parent, url, title, city, **kwargs):
        self.base_link = base_link
        self.api_link = api_link
        self.parent = parent
        self.url = url
        self.title = title
        self.city = city
        self.kwargs = kwargs

nofluffjobs = webSelectors(base_link="https://nofluffjobs.com/pl/job/",
                   api_link="https://nofluffjobs.com/api/posting/",
                   parent="postings",
                   url="url",
                   title="title",
                   city="city",
                   city_parent ="location",
                   city_parent2="places")

justjoin = webSelectors(base_link="https://justjoin.it/offers/",
                   api_link="https://justjoin.it/api/offers",
                   parent="",
                   url="id",
                   title="title",
                   city="city")


