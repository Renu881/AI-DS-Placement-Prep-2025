try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("File read successfully!")
finally:
    print("Execution completed.")

#Try-Except block is used to catch errors during file operations.
#finally is always executed, whether there is an exception or not.
