import datetime


def convert_date_format(date_str):
    formats_to_try = ["%d/%m/%Y", "%Y-%m-%d"]

    for date_format in formats_to_try:
        try:
            date_obj = datetime.datetime.strptime(date_str, date_format)
            return date_obj.strftime("%d-%m-%Y")
        except ValueError:
            pass

    return date_str  # Return the original string if no valid format is found


def convert_dates_in_list(list_of_dicts):
    for dictionary in list_of_dicts:
        for key, value in dictionary.items():
            if isinstance(value, str):
                dictionary[key] = convert_date_format(value)


