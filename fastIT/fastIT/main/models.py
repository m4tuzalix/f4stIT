from django.db import models
main_cities = (
    "Remote",
    "Wrocław",
    "Warszawa",
    "Poznań",
    "Kraków",
    "Katowice",
    "Łódź"
)
class Job(models.Model):
    link = models.TextField(unique=True, db_index=True, max_length=300)
    position = models.TextField(max_length=100)
    city = models.TextField(max_length=30, blank=True)

    def __str__(self):
        return self.link