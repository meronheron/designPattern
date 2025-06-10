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