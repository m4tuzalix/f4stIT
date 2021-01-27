class scraperSelectors:
    def __init__(self, main, link, possition, city):
        self.main = main
        self.link = link
        self.possition = possition
        self.city = city

linkedin = scraperSelectors(main="li[class='result-card job-result-card result-card--with-hover-state']",
                            link="a[class='result-card__full-card-link']",
                            possition="span[class='screen-reader-text']",
                            city="span[class='job-result-card__location']")

pracuj = scraperSelectors(main="div[class='offer__info']",
                          link="a[class='offer-details__title-link']",
                          possition="a[class='offer-details__title-link']",
                          city="li[class='offer-labels__item offer-labels__item--location']")

__all__ = ['linkedin', 'pracuj']