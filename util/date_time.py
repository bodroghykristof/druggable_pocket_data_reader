from datetime import datetime


def get_time():
    """Format current time"""

    return datetime.now().strftime("%H:%M:%S")
