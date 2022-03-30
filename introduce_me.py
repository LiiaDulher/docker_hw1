import datetime
import pytz


def main():
    timezone = pytz.timezone("Europe/Kiev")
    now = datetime.datetime.now(timezone)
    print("Current date and time : ", now.strftime("%H:%M:%S %d-%m-%Y"))
    print("My name and surname : Liia Dulher")


if __name__ == "__main__":
    main()
