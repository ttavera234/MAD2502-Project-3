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


def load_data(start_year: str, end_year: str, epidemic: str, by_nation: bool, state_list: list[str], age_group: tuple[str] = "A", file_name: str = "Covid.csv") -> None:
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
        obj: dict = {
            '2023 Covid Deaths': 0
        }
        for lines in csv_file:
            if lines['Year'] == '2023' and lines['COVID-19 Deaths']:
                obj['2023 Covid Deaths'] += int(lines['COVID-19 Deaths'])
            #obj['Date'] = lines['Data As Of']
            #print(lines)
        print(obj)

        #print(obj)


def query_data() -> None:
    """
        Description:
            ...

        Args:
            ...

        Returns:
            ...
        """

    # Handling user input -> https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
    time_range: list[str] = input(
        "Enter the range of years you wish to study in the following format 'YYYY-YYYY': ").split("-")
    epidemic: str = input(
        "Enter the epidemic you wish to study in the following format 'C' for COVID-19, 'I' for Influenza, or 'P' for Pneumonia: ")
    graph_decision: str = input(
        "Enter 'A' if you wish to study a national graph and 'B' if you wish to study a state graph: ")
    if graph_decision == 'A':
        list_of_states: list[str] = input(
            "Enter two or more states you wish to study in the following comma-separated format 'CA, FL, MI': ").split(", ")
        load_data()
    else:
        state: str = input(
            "Enter the state you wish to study in the following format 'FL' : ")
        group_decision: str = input(
            "Enter 'G' if you wish to focus on gender or 'A' if you wish to focus on a specified age group: ")
        if group_decision == 'A':
            age_groups: list[str] = input(
                "Enter the age groups you wish to study in the following comma-separated format '0-17, 18-29, 30-49, 50-64, 65-84': ").split(", ")


query_data()