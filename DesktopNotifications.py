import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Alert!!",
            message = "Take a break,... If u weren't already on a break",
            timeout = 10
        )
        time.sleep(3600)