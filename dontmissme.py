from tinydb import TinyDB, Query, where
from datetime import *
from supermemo2 import SMTwo

DB_DEFAULT = 'database.js'

def db_init(db_name):
    db = TinyDB(db_name)
    return db

## def db_save(topic):

def date_to_string(date):
    date_string = str(date.year) + '-' + str(date.month) + '-' + str(date.day)

    return date_string

def add_topic(db):
    rev_score = 0
    title = input("Enter the title for your new topic: ")
    desc = input("Write down a short description (press ENTER to leave blank): ")
    if len(desc.strip(" "))==0:
        desc == 'None'

    date_obj = date.today()
    revision_obj=SMTwo.first_review(3) #automatically sets today's date as add date

    date_add = date_to_string(date_obj)
    date_next = date_to_string(revision_obj.review_date)

    subject = input("Subject's name: ")
    db_id = db.insert({'title':title, 'desc':desc, 'add_date':date_add, 'last_date':date_add,
                    'next_date':date_next, 'easiness':revision_obj.easiness, 'interval':revision_obj.interval,
                    'repetitions':revision_obj.repetitions, 'subject':subject})
    
    return db_id

# Search of topics to revise today

def revise_today(db):
    today = date.today()
    today_date = date_to_string(today)

    args = db.search(where('next_date') == today_date)
    if(len(args)>0):
        return args
    else:
        return None

# Simple function that applies the SM2 algorithm to a specified topic

def revise_topic(db, topic_id, difficulty):
    topic_obj = db.get(doc_id=topic_id)
    topic_easiness = topic_obj['easiness']
    topic_repetitions = topic_obj['repetitions']
    topic_interval = topic_obj['interval']
    review_obj = SMTwo(topic_easiness, topic_interval, topic_repetitions).review(difficulty)
    update_topic(db, review_obj, topic_id)

    return

# Applying revise_topic changes to the actual db

def update_topic(db_obj, review_obj, topic_id):
    date_next = date_to_string(review_obj.review_date)
    today_is_last = date.today()
    last_date = date_to_string(today_is_last)

    db_obj.update({'last_date':last_date}, doc_ids=[topic_id])
    db_obj.update({'next_date':date_next}, doc_ids=[topic_id])
    db_obj.update({'easiness':review_obj.easiness}, doc_ids=[topic_id])
    db_obj.update({'interval':review_obj.interval}, doc_ids=[topic_id])
    db_obj.update({'repetitions':review_obj.repetitions}, doc_ids=[topic_id])

    print("Updated!")
    
    return

    
def main():
    db_main = db_init(DB_DEFAULT)
    all_subj = set()
    #topic_id = add_topic(db_main)

    topics_to_revise = revise_today(db_main)
    if topics_to_revise == None:
        print("Non ci sono argomenti da ripassare oggi.")
    else:
        print("Devi ripassare i seguenti argomenti: ")
        i=1
        for item in topics_to_revise:
            print("%d - %s" %(i, item['title']))
            i+=1
    try:
        user_input = int(input("\nWhich topic would you like to revise? "))
    except:
        print("Invalid input")
        exit()
    
    if user_input in range(1, i):
        revise_topic(db_main, topics_to_revise[user_input-1].doc_id, 3)
    else:
        print("Invalid choice.")
        exit()







main()