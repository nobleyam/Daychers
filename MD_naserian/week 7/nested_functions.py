import os  # Importing the os module for interacting with the operating system
import sys  # Importing the sys module to allow exiting the program if needed

# Define a function to list all contents (files and directories) inside a given path
def list_all_content(path):

    # This is an inner (nested) function to recursively list directory contents
    def list_directory(d):
        nonlocal inserted_tabs  # Allow this nested function to modify the variable from the outer function

        # Get all items (files and directories) in the current directory
        all_content = os.listdir(d)

        for item in all_content:
            # Construct the full path for the current item
            current_path = os.path.join(d, item)

            if os.path.isdir(current_path):
                # If the item is a directory, increase tab level and print it
                inserted_tabs += 1
                print('\t' * inserted_tabs, '[DIRECTORY]: ', item)

                # Recursively call list_directory to go deeper into the directory
                list_directory(current_path)

                # After finishing the inner directory, decrease tab level
                inserted_tabs -= 1
            else:
                # If the item is a file, just print it with the current tab level
                print('\t' * inserted_tabs, '[FILE]: ', item)

    inserted_tabs = 0  # Used to manage indentation level for nested directories

    if os.path.exists(path):  # Check if the provided path exists
        print('\t' * inserted_tabs, '[DIRECTORY]: ', path)  # Print the root directory
        list_directory(path)  # Start the recursive listing from the root path
    else:
        print('Path does not exist')  # Print an error if path doesn't exist
        sys.exit(-1)  # Exit the program with error code -1

# This is the main entry point of the script
if __name__ == '__main__':
    # Start listing contents from the current directory ('.')
    list_all_content('.')


# LEGB
# Local, Enclosing, Global, Builtins