file_path = "output.txt"

# Take user input and write it to the file
user_input = input("Enter text to write to the file: ")
with open(file_path, "w") as file:
    file.write(user_input + "\n")

# Take additional input and append it to the file
additional_input = input("Enter additional text to append to the file: ")
with open(file_path, "a") as file:
    file.write(additional_input + "\n")

# Read and display the final content of the file
with open(file_path, "r") as file:
    content = file.read()
    print("\nFinal content of the file:")
    print(content)