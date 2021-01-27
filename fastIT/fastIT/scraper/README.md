# python_job_reporter v1.1

# Requirements
- Python 3.x
- Chrome browser (chromedriver.exe in repo is for version 80)
- If your chrome's version is different, download the proper chromedriver.exe version https://chromedriver.chromium.org/
- Replace the just downloaded driver with the one currently exisiting in repo

# How to run
- Clone/download this repo
- Open repo directory in cmd/powershell (lshift+rclick -> copy as path -> type in terminal "cd <paste the path here>" -> enter)
- type in terminal pip install -r requirements.txt
- to run the script, use the command "python starter.py"
- Script will return "Finished" in terminal once it has finished the job

# Setup
- open starter.py in your editor
- find variable 'city' and put the city you are interested about
- find variable 'key_words' and put as many words as you want. I recommend max 3.

# Info
- Scraper gathers the offers from given websites and based on keywords creates the report
- Scraper is based on simple slite3 db which holds the data to avoid the duplicates
- DB clears itself every day
- Scraper creates one xls file per day and edits it (if already existing then appends new data)
- Scraper can by run any time :)

# v1.1
- Added one new website to scrap (nofluffjobs)
- Added remote scraping(requests based)
- fixed linkedin scraping(structure of the website has changed) 

# Update 13.04.2020
- fixed linkedin again

# Update 17.04.2020
- added 4th portal

# Update 18.04.2020
- fixed nofluff jobs

# Update 27.04.2020
- fixed pracuj
- added new column to excel (Position name) for easier use




