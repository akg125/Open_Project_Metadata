from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate(db)

# import pymongo


# client = pymongo.MongoClient("mongodb://localhost:27017/users")
# db = client['metadata-ms']
# collection = db['userCollection']