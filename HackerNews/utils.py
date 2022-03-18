import pymongo
def get_db_client():
    client = pymongo.MongoClient('mongodb+srv://hacker-news-hn22d.uq0bw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    return client