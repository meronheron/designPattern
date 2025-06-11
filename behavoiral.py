#command
from abc import ABC, abstractmethod
class TV:#reciever 
    def __init__(self):
        self.is_on = False
        self.channel = 1
    def turn_on(self):
        self.is_on = True
        print("TV is now turned on.")
    def turn_off(self):
        self.is_on = False
        print("TV is now turned off.")
    def change_channel(self, channel):
        if self.is_on:
            self.channel = channel
            print(f"Channel changed to {channel}.")
        else:
            print("TV is off. Please turn it on first.")
    def get_state(self):#return the state of the tv
        return self.is_on, self.channel