from tinydb import TinyDB, Query, where
from datetime import *
DB_DEFAULT = 'database.js'
SPACED_DAYS = []
for i in range(50):
    days = i*2+1
    print(i*2)
    SPACED_DAYS.append(days)
print(SPACED_DAYS)
    

'''
class Topic:
    def __init__(self, title, description, add_date, subject):
        self.title = title
        self.description = description
        self.add_date = add_date
        self.last_date = add_date
        self.next_date = (the followin day)
        self.rev_score = 0
        self.subject = subject
    
    def update_title(self, newtitle):
        self.title = newtitle

    def update_rev(self, date):
        self.rev_score += 1
        self.last_date = date
'''

def db_init(db_name):
    db = TinyDB(db_name)
    return db

## def db_save(topic):

def add_topic(db):
    rev_score = 0
    title = input("Enter the title for your new topic: ")
    desc = input("Write down a short description (press ENTER to leave blank): ")
    if len(desc.strip(" "))==0:
        desc == 'None'
    date_obj = date.today()
    date_add = str(date_obj.day) + '-' + str(date_obj.month) + '-' + str(date_obj.year)
    next_date_obj = date_obj + timedelta(days=SPACED_DAYS[rev_score])
    next_date = str(next_date_obj.day) + '-' + str(next_date_obj.month) + '-' + str(next_date_obj.year)
    subject = input("Subject's name: ")
    db_id = db.insert({'title':title, 'desc':desc, 'add_date':date_add, 'last_date':date_add,
                    'next_date':next_date, 'rev_score':rev_score, 'subject':subject})
    
    return db_id

#def spaced(topic):

    
def main():
    db_main = db_init(DB_DEFAULT)
    all_subj = set()
    db_id = add_topic(db_main)

main()