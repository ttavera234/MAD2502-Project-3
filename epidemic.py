from dataclasses import dataclass
import csv


@dataclass
class EpidemicData:
    start_date: str
    end_date: str
    grouping: str
    year: str
    month: str
    state: str
    sex: str
    age_group: str
    covid_deaths: str
    pneumonia_deaths: str
    influenza_deaths: str


class Epidemic:
    def __init__(self, name: str, month: str, year: str, sex_category: str, age_group: str, death_count: str):
        self._name: str = name
        self._month: str = month
        self._year: str = year
        self._sex_category: str = sex_category
        self._age_group: str = age_group
        self._death_count: int = int(death_count)


def handle_csv_data(file_name: str) -> None:
    """
    Description:
        ...

    Args:
        file_name: ...

    Returns:
        ...
    """

    # From GeeksForGeeks (https://www.geeksforgeeks.org/reading-csv-files-in-python/)
    with open(file_name, mode = "r") as file:
        csv_file = csv.DictReader(file)
        for lines in csv_file:
            print(lines)


handle_csv_data("covid.csv")
