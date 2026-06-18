from pymongo import MongoClient
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