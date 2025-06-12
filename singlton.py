#creational design pattern
## class that implements the Singleton pattern to ensure only one instance exists
class GameSettings:
    # Private class variable to store the single instance
    _instance = None
    # Static method to get the single instance (like a gatekeeper)
    @staticmethod
    def get_instance():
        # Check if no instance exists
        if GameSettings._instance is None:
            GameSettings._instance = GameSettings() # create single instance
        # Return the single instance
        return GameSettings._instance

    # Private constructor to control creation
    def __init__(self):
        if not hasattr(self, '_initialized'):  # Initialize settings only once
            self.volume = 50  # Default volume level
            self._initialized = True
    #get the volume level
    def get_volume(self):
        return self.volume
    
    def set_volume(self, volume):# Method to set the volume level
        self.volume = volume

if __name__ == "__main__":
    # Try to create two game settings instances
    settings1 = GameSettings.get_instance()
    settings2 = GameSettings.get_instance()

    # Check if they are the same instance
    print(settings1 is settings2)  # True (same settings object)

    # Check initial volume
    print(f"Settings 1 volume: {settings1.get_volume()}")  # 50
    print(f"Settings 2 volume: {settings2.get_volume()}")  # 50

    # Change volume using settings1
    settings1.set_volume(75)
    print(f"After change, Settings 1 volume: {settings1.get_volume()}")  # 75
    print(f"After change, Settings 2 volume: {settings2.get_volume()}")  # 75