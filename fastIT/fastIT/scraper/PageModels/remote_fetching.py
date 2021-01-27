from scraper.Imports import AsyncHTMLSession, requests
from scraper.Imports import findall

class RemoteScraper(AsyncHTMLSession):
    __slots__ = ["data", "web", "baselink", "first_link"]
    def __init__(self, web="linkedin", base_link=None, first_db_link=None, selector=None):
        AsyncHTMLSession.__init__(self)
        """
        :param str: web -> type of scrap:
        :param str: base_link -> parent element for offers:
        :param kwargs -> other selectors:
        """

        self.data = []
        self.web = web
        self.base_link = base_link
        self.first_db_link = first_db_link
        self.selector = selector
        self.stop = False

    async def _get_html(self, link):
        """
        returns page html(str)
        :param str: link -> page:
        :return requests.get(link).text:
        """
        source = await self.get(link)
        return source

    async def _get_concrete_element(self, parent, selector):
        return parent.find(selector, first=True)

    async def _scrap_data(self, instance):
        """
        scrap all available offers within the page and appends new tuple(link, title) to global array -> self.data
        :param object: instance -> bs instance:
        :return:
        """
        try:
            for offer in instance.html.find(self.selector.main):
                try:
                    link = await self._get_concrete_element(offer, self.selector.link)
                    if self.first_db_link != None:
                        if self.first_db_link in link.attrs["href"]:
                            self.stop = True
                            break
                    possition = await self._get_concrete_element(offer, self.selector.possition)
                    city =  await self._get_concrete_element(offer, self.selector.city)
                    if "lokal" in city.text:
                        city = ""
                    elif "," in city.text:
                        city = city.text.split(",")[0]
                    else:
                        city = city.text
                    self.data.append((link.attrs["href"], possition.text, city))
                except Exception as e:
                    print(str(e))
                    continue
        except Exception as e:
            print(f"Error occured when fetching {self.web}: "+str(e)+", but continued")

    def _get_loop_range(self):
        """
        Estimates how the loop should iterate basing on self.web argument (2 ways)
        :return loop_range:
        """
        loop_range = None
        if self.web == "linkedin":
            loop_range = (1, 999, 25)
        elif self.web == "nfj" or self.web == "pracuj":
            link_for_regex =  requests.get(self.base_link+"1").text
            try:
                pattern = r'[/>] (\d{2})'
                if self.web == "nfj":
                    pattern = r'(\d+\.?\d*) </a></li>'
                regex = findall(pattern, link_for_regex) # regex for the last page number from pagination
                loop_range = int(regex[-1])
            except IndexError:
                raise
        else:
            raise  AttributeError("Only linkedin or nfj or pracuj accepted")
        return loop_range

    async def _main_loop(self, page_range):
        """
        Main mechanism. Returns complete list of data from the website
        :return self.data:
        """
        print(page_range)
        try:
            for x in range(*page_range): # unpacks tuple
                try:
                    source_html = await self._get_html(self.base_link+str(x))
                except:
                    continue
                if self.stop != True:
                    await self._scrap_data(source_html)
                else:
                    await self.close()

        except IndexError:
            print("Regex did not find")

    def _task_creator(self, iterations=5):
        from math import ceil
        tasks = []
        loop_range = self._get_loop_range()
        if self.web == "linkedin":
            pages_devided = ceil(loop_range[1]/iterations)
            rest = pages_devided % 10
            if rest < 5:
                pages_devided -= rest
            else:
                pages_devided += (10 - rest)
            x,y,z = 25, pages_devided, 25
        else:
            pages_devided = ceil(loop_range/iterations)
            x,y,z   = 1, pages_devided, 1
        for r in range(iterations):
            async def main_loop_prototype(page_range = (x,y,z)):
                await self._main_loop(page_range)
            tasks.append(main_loop_prototype)
            x+=pages_devided
            y+=pages_devided
        return tasks

    def trigger(self):
        print(f"Scrapping {self.web}")
        self.run(*self._task_creator())
