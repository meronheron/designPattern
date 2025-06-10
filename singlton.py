# creational design pattern
## create class that implements the Singleton pattern to ensure only one instance exists.
class President:
    # Class variable to store the single instance
    _instance = None
    #controls instance creation, ensuring only one instance is created
    def __new__(cls, name):
     # Check if a president instance already exists
        if cls._instance is None:
            # Create a new instance if none exists
            cls._instance = super(President, cls).__new__(cls)
        # Return the single instance
        return cls._instance
    def __init__(self, name):
        # initialize the president's attributes (only if not already initialized)
        if not hasattr(self, '_initialized'):
            self.name = name
            self._initialized = True
    def get_name(self):
        # Return the president's name
        return self.name

    def set_name(self, name):
        # update the president's name (e.g., after an election)
        self.name = name
if __name__ == "__main__":
    # attempt to create two presidents
    president1 = President("Abraham lincoln")
    president2 = President("Bill Cliton")
# check if they are the same instance
    print(president1 is president2)  # True
    print(f"President 1: {president1.get_name()}")  # Abraham lincoln
    print(f"President 2: {president2.get_name()}") # Abraham lincoln
# change the president's name (simulating a new election)
    president1.set_name("Barack Obama")
    print(f"After election, President 1: {president1.get_name()}")  # Barack Obama
    print(f"After election, President 2: {president2.get_name()}")  # Barack Obama