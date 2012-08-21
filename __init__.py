from instances import Instances
from modifications import Modifications

class DateTimeLibrary(Instances, Modifications):
    """
    Library for interacting with the date and time
    """
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    
    def __init__(self):
        super(DateTimeLibrary, self).__init__()