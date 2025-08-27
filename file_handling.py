try:
    # Open and read the file
    with open("sample.txt", "r") as file:
        # Print content line by line
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")