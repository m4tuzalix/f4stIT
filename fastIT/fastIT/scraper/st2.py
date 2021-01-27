from Pages.main import JustJoinIt, RemoteModel
import asyncio
import nest_asyncio


class Starter:
    def __init__(self):
        self._final_links = []
        self.models = (
            RemoteModel(base_link="https://www.pracuj.pl/"\
                        "praca/it%20-%20rozw%c3%b3j%20oprogramowania;cc,5016?pn=", web="pracuj"),
            RemoteModel(base_link="https://pl.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/"\
                        "information-technology-jobs-k%C4%85ty-"\
                        "wroc%C5%82awskie?trk=homepage-jobseeker_suggested-search&start=", web="linkedin"),
            RemoteModel(base_link="https://nofluffjobs.com/pl/jobs/backend?"\
                        "criteria=category%3Dfrontend,fullstack,"\
                        "mobile,testing,devops,embedded,security,gaming", web="nfj"),
            JustJoinIt()
        )

    def _fetch_links(self):
        return self._final_links

    async def _task_pattern(self, model : RemoteModel):
        await asyncio.sleep(1)
        self._final_links.extend(model.fetching_data())

    async def _task_creator(self):
        _all_tasks = []
        for task in self.models:
            _all_tasks.append(asyncio.create_task(self._task_pattern(task)))
        await asyncio.gather(*_all_tasks)

    def run_asyncio(self):
        asyncio.run(self._task_creator())
        return self._fetch_links()

if __name__ == "__main__":
    nest_asyncio.apply()
    start = Starter()
    start.run_asyncio()

