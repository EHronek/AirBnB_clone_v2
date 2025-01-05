from os import getenv

type_storage = getenv("HBNB_TYPE_STORAGE")

if type_storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

