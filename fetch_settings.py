import shelve

FILE_NAME = ".fetch-settings"
DATE_KEY = "date"


def read_last_date():
    file = shelve.open(FILE_NAME)

    if (DATE_KEY in file):
        val = file[DATE_KEY]
        file.close()
        return val
    else:
        file.close()
        raise KeyError("Key not found")


def write_last_date(date):
    file = shelve.open(FILE_NAME)

    file[DATE_KEY] = date

    file.close()