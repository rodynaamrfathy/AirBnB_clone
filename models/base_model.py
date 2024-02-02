#!/usr/bin/python3
""" base model defines all common attributes/methods for other classes. """
import uuid
from datetime import datetime

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
    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        dic = self.__dict__.copy()
        dic['__class__'] = type(self).__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
