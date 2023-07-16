#!/usr/bin/python3
"""Module for FileStorage autoinit. Done"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
