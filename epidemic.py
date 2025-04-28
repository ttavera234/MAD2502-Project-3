import csv

from dataclasses import dataclass
from histogram import plot_histogram


@dataclass
class EpidemicData:
    name: str
    deaths: list[int]
    years: list[str]
    states: list[str]
    age_groups: list[str]
    sexes: list[str]


def create_csv_file(file_type: str, file_name: str = "Covid.csv") -> None:
    """
        Description:
            ...

        Args:
            file_type: ...
            file_name: ...

        Returns:
            ...
    """

    d: list[dict] = []

    # Reading from CSV files from GeeksForGeeks (https://www.geeksforgeeks.org/reading-csv-files-in-python/)
    with open(file_name, mode="r") as file:
        csv_file = csv.DictReader(file)
        for lines in csv_file:
            if lines["Group"] == "By Year" and (
                    lines["State"] != "United States" and lines["State"] != "District of Columbia" and
                    lines["State"] != "New York City" and lines["State"] != "Puerto Rico"):
                if file_type == 'N' and lines["Sex"] == "All Sexes" and lines["Age Group"] == "All Ages":
                    if not lines["COVID-19 Deaths"]:
                        lines["COVID-19 Deaths"] = "1-9"
                    elif not lines["Pneumonia Deaths"]:
                        lines["Pneumonia Deaths"] = "1-9"
                    elif not lines["Influenza Deaths"]:
                        lines["Influenza Deaths"] = "1-9"

                    d.append(
                        {"Year": lines["Year"], "State": lines["State"], "COVID-19 Deaths": lines["COVID-19 Deaths"],
                         "Pneumonia Deaths": lines["Pneumonia Deaths"], "Influenza Deaths": lines["Influenza Deaths"]}
                    )

                elif file_type == "SG" and lines["Sex"] != "All Sexes" and lines["Age Group"] == "All Ages":
                    if not lines["COVID-19 Deaths"]:
                        lines["COVID-19 Deaths"] = "1-9"
                    elif not lines["Pneumonia Deaths"]:
                        lines["Pneumonia Deaths"] = "1-9"
                    elif not lines["Influenza Deaths"]:
                        lines["Influenza Deaths"] = "1-9"

                    d.append(
                        {"Year": lines["Year"], "State": lines["State"], "Sex": lines["Sex"],
                         "COVID-19 Deaths": lines["COVID-19 Deaths"],
                         "Pneumonia Deaths": lines["Pneumonia Deaths"], "Influenza Deaths": lines["Influenza Deaths"]}
                    )

                elif file_type == "SA" and lines["Sex"] == "All Sexes" and (
                        lines["Age Group"] == "0-17 years" or lines["Age Group"] == "18-29 years" or lines[
                    "Age Group"] == "30-39 years" or
                        lines["Age Group"] == "40-49 years" or lines["Age Group"] == "50-64 years" or lines[
                            "Age Group"] == "65-74 years" or
                        lines["Age Group"] == "75-84 years" or lines["Age Group"] == "85 years and over"):

                    if not lines["COVID-19 Deaths"]:
                        lines["COVID-19 Deaths"] = "1-9"
                    elif not lines["Pneumonia Deaths"]:
                        lines["Pneumonia Deaths"] = "1-9"
                    elif not lines["Influenza Deaths"]:
                        lines["Influenza Deaths"] = "1-9"

                    d.append(
                        {"Year": lines["Year"], "State": lines["State"], "Age Group": lines["Age Group"],
                         "COVID-19 Deaths": lines["COVID-19 Deaths"], "Pneumonia Deaths": lines["Pneumonia Deaths"],
                         "Influenza Deaths": lines["Influenza Deaths"]}
                    )

    # Writing to CSV files from GeeksForGeeks (https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/)
    new_file: str = ""
    f = []
    if file_type == 'N':
        new_file = "N_data.csv"
        f = ["Year", "State", "COVID-19 Deaths", "Pneumonia Deaths", "Influenza Deaths"]
    elif file_type == "SG":
        new_file = "SG_data.csv"
        f = ["Year", "State", "Sex", "COVID-19 Deaths", "Pneumonia Deaths", "Influenza Deaths"]
    elif file_type == "SA":
        new_file = "SA_data.csv"
        f = ["Year", "State", "Age Group", "COVID-19 Deaths", "Pneumonia Deaths", "Influenza Deaths"]

    with open(new_file, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=f)
        writer.writeheader()
        writer.writerows(d)


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

    ### TODO: verify that the time range is between [2020, 2023]

    epidemic: str = input(
        "Enter the epidemic you wish to study, your options are: COVID-19, Influenza, or Pneumonia: ")

    ### TODO: verify that the epidemic input is either "COVID-19", "Influenza", or "Pneumonia"

    graph_decision: str = input(
        "Enter 'N' if you wish to study a national graph and 'S' if you wish to study a state graph: ")

    ### TODO: verify that the graph decision input is either "N" or "S"

    if graph_decision == 'N':
        state_list: list[str] = input(
            "Enter two or more states you wish to study in the following comma-separated format 'California, Florida': ").split(", ")

        # TODO: Verify that the states inputted are valid/exist in the "N_data.csv" data set

        load_data_into_structure(file_type="N", time_range=time_range, epidemic=epidemic, state_list=state_list)
    else:
        state: str = input(
            "Enter the state you wish to study in the following format 'Florida' : ")

        # TODO: Verify that the state inputted is valid/exist in either the "SA_data.csv" or "SG_data.csv" data sets

        group_decision: str = input(
            "Enter 'G' if you wish to focus on gender or 'A' if you wish to focus on a specified age group: ")

        ### TODO: verify that the group decision input is either "G" or "A"

        if group_decision == 'A':
            age_groups: list[str] = input(
                "Enter the age groups you wish to study in the following comma-separated format: 0-17 years, 18-29 years, "
                                                                                                "30-39 years, 40-49 years, "
                                                                                                "50-64 years, 65-74 years, "
                                                                                                "75-84 years, or 85 years and over: ").split(", ")

            # TODO: Verify that the age groups inputted are valid/exist in the "SA_data.csv" data set

            load_data_into_structure(file_type="SA", time_range=time_range, epidemic=epidemic, state_list=[state], age_groups=age_groups)
        else:
            load_data_into_structure(file_type="SG", time_range=time_range, epidemic=epidemic, state_list=[state])


def load_data_into_structure(file_type: str, time_range: list[str], epidemic: str, state_list: list[str], age_groups: list[str] = "All") -> None:
    """
        Description:
            ...

        Args:
            file_type: ...
            time_range: ...
            epidemic: ...
            state_list: ...
            age_groups: ...

        Returns:
            ...
    """

    if file_type == 'N':
        epidemic_data: EpidemicData = EpidemicData(
            name=epidemic, years=time_range, states=state_list,
            age_groups=age_groups, sexes=["Male", "Female"], deaths=[0] * len(state_list)
        )

        with open("N_data.csv", mode="r") as file:
            csv_data = csv.DictReader(file)
            for index, state in enumerate(epidemic_data.states):
                for lines in csv_data:
                    if lines["State"] == state and epidemic_data.years[0] <= lines["Year"] <= epidemic_data.years[1]:
                        calculate_epidemic_deaths(epidemic_data=epidemic_data, lines=lines, death_index=index)
                file.seek(0) # Returns to the beginning of the file to calculate the deaths of a different state

        plot_histogram(
            x_axis=epidemic_data.states, y_axis=epidemic_data.deaths, x_label="States",
            title=f"{epidemic_data.name} Cases Between {epidemic_data.years[0]}-{epidemic_data.years[1]}"
        )

    elif file_type == "SG":
        epidemic_data: EpidemicData = EpidemicData(
            name=epidemic, years=time_range, states=state_list,
            age_groups=age_groups, sexes=["Male", "Female"], deaths=[0] * 2
        )

        with open("SG_data.csv", mode="r") as file:
            csv_data = csv.DictReader(file)
            for index, gender in enumerate(epidemic_data.sexes):
                for lines in csv_data:
                    if lines["Sex"] == gender and lines["State"] == epidemic_data.states[0] and epidemic_data.years[0] <= lines["Year"] <= epidemic_data.years[1]:
                        calculate_epidemic_deaths(epidemic_data=epidemic_data, lines=lines, death_index=index)
                file.seek(0)  # Returns to the beginning of the file to calculate the deaths of a different gender

        plot_histogram(
            x_axis=epidemic_data.sexes, y_axis=epidemic_data.deaths, x_label="Gender",
            title=f"{epidemic_data.states[0]} {epidemic_data.name} Cases Based On Gender Between {epidemic_data.years[0]}-{epidemic_data.years[1]}"
        )

    elif file_type == "SA":
        epidemic_data: EpidemicData = EpidemicData(
            name=epidemic, years=time_range, states=state_list,
            age_groups=age_groups, sexes=["Male", "Female"], deaths=[0] * len(age_groups)
        )

        with open("SA_data.csv", mode="r") as file:
            csv_data = csv.DictReader(file)
            for index, age_group in enumerate(epidemic_data.age_groups):
                for lines in csv_data:
                    if lines["Age Group"] == age_group and lines["State"] == epidemic_data.states[0] and epidemic_data.years[0] <= lines["Year"] <= epidemic_data.years[1]:
                        calculate_epidemic_deaths(epidemic_data=epidemic_data, lines=lines, death_index=index)
                file.seek(0)

        plot_histogram(
            x_axis=epidemic_data.age_groups, y_axis=epidemic_data.deaths, x_label="Age Groups",
            title=f"{epidemic_data.states[0]} {epidemic_data.name} Cases Based On Different Age Groups Between {epidemic_data.years[0]}-{epidemic_data.years[1]}"
        )


def calculate_epidemic_deaths(epidemic_data: EpidemicData, lines: dict[str, str], death_index: int) -> None:
    """
        Description:
            ...

        Args:
            epidemic_data: ...
            lines: ...
            death_index: ...

        Returns:
            ...
    """

    if lines[f"{epidemic_data.name} Deaths"] == "1-9":
        epidemic_data.deaths[death_index] += 1 # Takes minimum since it is the guaranteed data point
    else:
        try:
            epidemic_data.deaths[death_index] += int(lines[f"{epidemic_data.name} Deaths"])
        except ValueError:
            epidemic_data.deaths[death_index] += 0


def clean_data() -> None:
    # Cleaning data for easier parsing
    create_csv_file('N')
    create_csv_file("SG")
    create_csv_file("SA")


def main() -> None:
    while True:
        query_data()


if __name__ == "__main__":
    main()