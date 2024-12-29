from models import storage
from models.state import State

for key, obj in storage.all().items():
    if isinstance(obj, State):
        if not hasattr(obj, 'updated_at'):
            obj.updated_at = obj.created_at
            storage.save()

