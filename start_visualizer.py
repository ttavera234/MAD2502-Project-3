from epidemic import query_data


def main() -> None:
    """
        Description:
            Main function where our application will run from. Runs in an infinite loop until user commands it to "Stop"
    """

    while True:
        query_data()


if __name__ == "__main__":
    main()