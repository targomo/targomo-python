import datetime
import math

class Util:
    'This class encapsulates generally useful methods from all sorts of domains'

    @staticmethod
    def currentDate():
        return datetime.datetime.now().strftime("%Y%m%d")

    @staticmethod
    def currentTime():

        now = datetime.datetime.now()
        seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        return int(math.ceil(seconds_since_midnight / 60.0)) * 60