import csv


def create_csv_file(file_type: str, file_name: str = "Covid.csv") -> None:
    """
        Description:
            Creates a CSV file based on the `file_type` parameter passed in.

        Args:
            file_type: Either "N", "SG", or "SA".
                An "N" filetype stores data based on multiple states and epidemic death count
                An "SG" filetype stores data based on a single state's death count based on gender
                An "SA" filetype stores data based on a single state's death count based on differing age groups
            file_name: Large dataset set that is going to be broken down into three smaller, more manageable ones
    """

    data_rows: list[dict] = []

    # Reading from CSV files from GeeksForGeeks (https://www.geeksforgeeks.org/reading-csv-files-in-python/)
    with open(file_name, mode="r") as file:
        csv_file = csv.DictReader(file)
        for lines in csv_file:
            if lines["Group"] == "By Year" and (
                    lines["State"] != "United States" and lines["State"] != "District of Columbia" and
                    lines["State"] != "New York City" and lines["State"] != "Puerto Rico"): # Getting all 50 US states for consistent data
                if file_type == 'N' and lines["Sex"] == "All Sexes" and lines["Age Group"] == "All Ages":
                    if not lines["COVID-19 Deaths"]: # Cleaning empty data
                        lines["COVID-19 Deaths"] = "1-9"
                    elif not lines["Pneumonia Deaths"]:
                        lines["Pneumonia Deaths"] = "1-9"
                    elif not lines["Influenza Deaths"]:
                        lines["Influenza Deaths"] = "1-9"

                    data_rows.append(
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

                    data_rows.append(
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

                    data_rows.append(
                        {"Year": lines["Year"], "State": lines["State"], "Age Group": lines["Age Group"],
                         "COVID-19 Deaths": lines["COVID-19 Deaths"], "Pneumonia Deaths": lines["Pneumonia Deaths"],
                         "Influenza Deaths": lines["Influenza Deaths"]}
                    )

    # Writing to CSV files from GeeksForGeeks (https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/)
    new_file: str = ""
    data_header: list[str] = []
    if file_type == 'N':
        new_file = "N_data.csv"
        data_header = ["Year", "State", "COVID-19 Deaths", "Pneumonia Deaths", "Influenza Deaths"]
    elif file_type == "SG":
        new_file = "SG_data.csv"
        data_header = ["Year", "State", "Sex", "COVID-19 Deaths", "Pneumonia Deaths", "Influenza Deaths"]
    elif file_type == "SA":
        new_file = "SA_data.csv"
        data_header = ["Year", "State", "Age Group", "COVID-19 Deaths", "Pneumonia Deaths", "Influenza Deaths"]

    with open(new_file, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_header)
        writer.writeheader()
        writer.writerows(data_rows)


def clean_data() -> None:
    """
        Description:
            Creates three new CSV files with more organized data for the purposes of our Epidemic visualization. Greatly simplifies logic and makes the data more understandable
    """

    create_csv_file('N')
    create_csv_file("SG")
    create_csv_file("SA")