#command
from abc import ABC, abstractmethod
class TV:#reciever 
    def __init__(self):
        self.is_on = False
        self.channel = 1