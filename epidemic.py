import csv
from dataclasses import dataclass
from histogram import plot_histogram

# Epidemic data structure
@dataclass
class EpidemicData:
    name: str
    deaths: list[int]
    years: list[str]
    states: list[str]
    age_groups: list[str]
    sexes: list[str]


def query_data() -> None:
    """
        Description:
            Queries the user for data, and then filters the dataset based on this data.
            After filtering, it then loads the data into the Epidemic Data Structure and visualizes it using a histogram.
    """

    # Handling user input -> https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
    time_range: list[str] = input(
        "Enter the range of years you wish to study in the following format 'YYYY-YYYY': ").split("-")

    #Verify that the time range is between [2020, 2023]
    if len(time_range) != 2 or not all(year.isdigit() for year in time_range) or not (2020 <= int(time_range[0]) <= 2023) or not (2020 <= int(time_range[1]) <= 2023):
        print("Invalid time range. Please enter years between 2020 and 2023.")
        return

    valid_epidemics = ["COVID-19", "Influenza", "Pneumonia"]
    
    epidemic: str = input(
        "Enter the epidemic you wish to study, your options are: COVID-19, Influenza, or Pneumonia: ")


    graph_decision: str = input(
        "Enter 'N' if you wish to study a national graph and 'S' if you wish to study a state graph: ")

    #Verify that the graph decision input is either "N" or "S"
    if graph_decision.upper() not in ["N", "S"]:
        print("Invalid choice. Enter 'N' or 'S'.")
        return

    if graph_decision == 'N':
        state_list: list[str] = input(
            "Enter two or more states you wish to study in the following comma-separated format 'California, Florida': ").split(", ")

        # TODO: Verify that the states inputted are valid/exist in the "N_data.csv" data set
        valid_states = [
            "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
    "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
        ]

        for state in state_list:
            if state.strip().title() not in valid_states:
                print(f"Invalid state entered: {state}")
                return

        load_data_into_structure(file_type="N", time_range=time_range, epidemic=epidemic, state_list=state_list)
    else:
        state: str = input(
            "Enter the state you wish to study in the following format 'Florida' : ")

        # TODO: Verify that the state inputted is valid/exist in either the "SA_data.csv" or "SG_data.csv" data sets
        valid_states = [  # Same valid states list
            "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
            "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
            "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
            "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
            "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
            "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
        ]

         if state.strip().title() not in valid_states:
            print(f"Invalid state entered: {state}")
            return

        group_decision: str = input(
            "Enter 'G' if you wish to focus on gender or 'A' if you wish to focus on a specified age group: ")

        #Verify that the group decision input is either "G" or "A"

        if group_decision.upper() not in ["G", "A"]:
            print("Invalid choice. Enter 'G' or 'A'.")
            return
        
        if group_decision == 'A':
            age_groups: list[str] = input(
                "Enter the age groups you wish to study in the following comma-separated format: 0-17 years, 18-29 years, "
                                                                                                "30-39 years, 40-49 years, "
                                                                                                "50-64 years, 65-74 years, "
                                                                                                "75-84 years, or 85 years and over: ").split(", ")

            #Verify that the age groups inputted are valid/exist in the "SA_data.csv" data set
            for age_group in age_groups:
                if age_group.strip() not in valid_age_groups:
                    print(f"Invalid age group entered: {age_group}")
                    return

            load_data_into_structure(file_type="SA", time_range=time_range, epidemic=epidemic, state_list=[state], age_groups=age_groups)
        else:
            load_data_into_structure(file_type="SG", time_range=time_range, epidemic=epidemic, state_list=[state])


def load_data_into_structure(file_type: str, time_range: list[str], epidemic: str, state_list: list[str], age_groups: list[str] = "All") -> None:
    """
        Description:
            Using the filters provided by the user, it constructs an Epidemic data structure consisting of:
                - A time range
                - A specific epidemic (name)
                - State(s) being studied
                - Age groups being studied

        Args:
            file_type: Either "N", "SG", or "SA".
                An "N" filetype loads the Epidemic data structure based on the list of states the user wants to study.
                An "SG" filetype loads the Epidemic data structure based on the impact gender had on the death count in a certain state.
                An "SA" filetype loads the Epidemic data structure based on the impact differing age groups had on the death count in a certain state.
            time_range: The range of years the user wants to study
            epidemic: The name of the epidemic the user wants to study
            state_list: The list of states the user wants to study
            age_groups: The various age groups the user wants to study
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
            Calculates the number of casualties from a given epidemic and stores the number in an appropriate list position for data visualization.

        Args:
            epidemic_data: The loaded data structure we are calculating the deaths for
            lines: The current line being parsed in the CSV file
            death_index: The index in the list of deaths that is currently being calculated
                e.g. ["Male", "Female"] --> [Male_Death_Count, Female_Death_Count]
    """

    if lines[f"{epidemic_data.name} Deaths"] == "1-9":
        epidemic_data.deaths[death_index] += 1 # Takes minimum since it is the guaranteed data point
    else:
        try:
            epidemic_data.deaths[death_index] += int(lines[f"{epidemic_data.name} Deaths"])
        except ValueError: # Special case when there isn't a data value (i.e. ==> '')
            epidemic_data.deaths[death_index] += 0

