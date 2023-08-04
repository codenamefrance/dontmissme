from tinydb import TinyDB, Query, where
from datetime import *
from supermemo2 import SMTwo, day_mon_year

DB_DEFAULT = 'database.js'

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

'''
The values are the:
Quality: The quality of recalling the answer from a scale of 0 to 5.
5: perfect response.
4: correct response after a hesitation.
3: correct response recalled with serious difficulty.
2: incorrect response; where the correct one seemed easy to recall.
1: incorrect response; the correct one remembered.
0: complete blackout.
Easiness: The easiness factor, a multipler that affects the size of the interval, determine by the quality of the recall.
Interval: The gap/space between your next review.
Repetitions: The count of correct response (quality >= 3) you have in a row.
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
    revision_obj=SMTwo.first_review(3) #automatically sets today's date as add date

    date_add = str(date_obj.day) + '-' + str(date_obj.month) + '-' + str(date_obj.year)
    date_next = str(revision_obj.review_date.year)+ '-' + str(revision_obj.review_date.month)+ '-' + str(revision_obj.review_date.day)

    subject = input("Subject's name: ")
    db_id = db.insert({'title':title, 'desc':desc, 'add_date':date_add, 'last_date':date_add,
                    'next_date':date_next, 'easiness':revision_obj.easiness, 'interval':revision_obj.interval,
                    'repetitions':revision_obj.repetitions, 'subject':subject})
    
    return db_id

def update_topic(db_obj, review_obj):
    date_next = str(review_obj.review_date.year)+ '-' + str(review_obj.review_date.month)+ '-' + str(review_obj.review_date.day)
    today_is_last = date.today()
    last_date = str(today_is_last.year) + '-' + str(today_is_last.month) + '-' + str(today_is_last.day)

    db_obj.update({'last_date':last_date})
    db_obj.update({'next_date':date_next})
    db_obj.update({'easiness':review_obj.easiness})
    db_obj.update({'interval':review_obj.interval})
    db_obj.update({'repetitions':review_obj.repetitions})

    print("Updated!")
    
    return

def revise_topic(db, topic_id, difficulty):
    topic_obj = db.get(doc_id=topic_id)
    print(topic_obj)
    topic_easiness = topic_obj['easiness']
    topic_repetitions = topic_obj['repetitions']
    topic_interval = topic_obj['interval']
    review_obj = SMTwo(topic_easiness, topic_interval, topic_repetitions).review(difficulty)
    update_topic(db, review_obj)

    return

#def funzione che cerca gli argomenti da ripassare in giornata, ritorna l'id nel db del topic

#def spaced(topic):

    
def main():
    db_main = db_init(DB_DEFAULT)
    all_subj = set()
    #topic_id = add_topic(db_main)

    revise_topic(db_main, 1, 3)




    

main()