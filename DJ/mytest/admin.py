from pymongo import MongoClient

# Register your models here.
from django.contrib import admin
from mytest.models import Music

admin.site.register(Music)

if __name__ == '__main__':
    client = MongoClient(
        "mongodb://127.0.0.1:27017/?directConnection=true",
    )
    db = client['myDatabase']
    collection = db['users']

    # 插入
    collection.insert_one({'name': 'Alice', 'age': 25})

    # 查询
    for doc in collection.find():
        print(doc)