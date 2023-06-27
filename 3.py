# file_operations.py
# Writing to a file
with open("data.txt", "w") as file:
    file.write("This is some data.")

# Reading from a file
with open("data.txt", "r") as file:
    data = file.read()
    print("Data:", data)

