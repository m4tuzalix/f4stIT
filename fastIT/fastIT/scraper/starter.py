import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from scraper.Pages.main import Model
from scraper.Database.database import DBconnection

class Starter:
    def __init__(self):
        self.db = DBconnection()
        self.db.db_main()
        self.db.check_db()
        self.pracuj = Model(base_link="https://www.pracuj.pl/praca/it%20-%20rozw%c3%b3j%20oprogramowania;cc,5016?pn=", web="pracuj", type="scraper")
        self.linkedin = Model(base_link="https://pl.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?location=Wroc%C5%82aw%2C%20Woj.%20Dolno%C5%9Bl%C4%85skie%2C%20Polska&trk=homepage-jobseeker_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0&f_PP=101782795%2C101832192%2C102513900%2C102560051%2C103348205&start=", web="linkedin", type="scraper")
        self.noflufjobs = Model(base_link="https://nofluffjobs.com/pl/job/", web="nofluffjobs", type="api")
        self.jji = Model(base_link="https://justjoin.it/offers/", web="justjoin", type="api")
        self.data = []

    def start_fetching(self):
        for site in self.pracuj, self.linkedin, self.noflufjobs, self.jji:
            self.data.extend(site.fetch_data())
        return self.data
