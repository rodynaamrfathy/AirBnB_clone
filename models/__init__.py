#!/usr/bin/python3

"""
This script creates a unique instance of a FileStorage class for your application.

FileStorage is responsible for managing the storage and retrieval of data within your application. By creating a unique instance, you ensure that your application has its own isolated storage environment.

The script initializes the FileStorage instance and then calls its reload() method. This method is typically used to reload data from storage or perform necessary initialization tasks, ensuring that the FileStorage instance is up-to-date and ready to be used by the application.

Usage:
    - Ensure that this script is executed using Python 3.
    - Import this script into your application to create a FileStorage instance.
"""

from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
