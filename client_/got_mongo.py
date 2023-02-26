import sys
import pymongo
import config

from pymongo import MongoClient


def get_client():
    client = pymongo.MongoClient(
       config.mongodb_url
    )
    db = client.get_database()
    return client


def t1():

    c = get_client()
    print(list(c.list_databases()))


if __name__ == "__main__":
    t1()