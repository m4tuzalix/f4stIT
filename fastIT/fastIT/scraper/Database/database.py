from sqlite3 import Connection

class DBconnection(Connection):
    def __init__(self):
        Connection.__init__(self, "main.db")
        self.cur = self.cursor()

    def db_main(self):
        """
        Creates the main table or clears existing from old records
        :return:
        """
        self.cur.execute("CREATE TABLE IF NOT EXISTS links(id INTEGER PRIMARY KEY, link TEXT, possition TEXT, city TEXT, web TEXT, date TEXT, time TEXT)")
        self.cur.execute("DELETE FROM links WHERE date != date('now')")
        self.commit()

    def check_db(self):
        self.cur.execute("SELECT * FROM links")
        if len(self.cur.fetchall()) > 0:
            self.cur.execute("DELETE FROM links WHERE id NOT IN (SELECT min(id) FROM links WHERE "
                             "instr(link, 'justjoin') OR "
                             "instr(link, 'nofluff') OR "
                             "instr(link, 'pracuj') OR "
                             "instr(link, 'linkedin') "
                             "GROUP BY web) ")
            self.commit()

class Database():
    def __init__(self, company=None, **args):
        """
        constructor establishes connection with sqlite db
        :param args:
        """
        self.db = DBconnection()
        self.cur = self.db.cursor()
        self.com = self.db.commit

        self.company = company

    def add_new_links(self, input):
        """
        Inserts new records into db
        :param str: link -> link from website:
        :param str: possition -> possition name:
        :return:
        """
        for single in input:
            self.cur.execute("INSERT INTO links VALUES(NULL,?,?,?,?,date('now'),time('now'))", (single[0], single[1], single[2], self.company, ))
        self.com()

    def get_first_available_link(self):
        """
        Returns the full content of db
        :param str: company -> name of website:
        :return generator:
        """
        self.cur.execute("SELECT link FROM links WHERE instr(link, ?)", (self.company,))
        link = self.cur.fetchone()
        self.com()
        return link[0] if link is not None else None


