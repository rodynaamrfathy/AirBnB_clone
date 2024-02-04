#!/usr/bin/python3
""" base model defines all common attributes/methods for other classes. """
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class for defining common attributes and methods.

    Attributes:
        id (str): Unique identifier generated using uuid.uuid4().
        created_at (datetime): Date and time of instance creation.
        updated_at (datetime): Date and time of the last update.

    Methods:
        __init__: Initializes the BaseModel instance with a unique id and timestamps.
        __str__: Returns a string representation of the instance.
        save: Updates the updated_at attribute with the current datetime.
        to_dict: Returns a dictionary representation of the instance.

    """
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

            Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        dic = self.__dict__.copy()
        dic['__class__'] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
