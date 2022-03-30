import datetime


def main():
    now = datetime.datetime.now()
    print("Current date and time : ", now.strftime("%H:%M:%S %d-%m-%Y"))
    print("My name and surname : Liia Dulher")


if __name__ == "__main__":
    main()
