import os

MAX_FILES_TO_DISPLAY = 3


def print_folder_structure(folder_path, indent=0):
    # Print the current folder with appropriate indentation
    print("  " * indent + "|---" + os.path.basename(folder_path))

    # List all files and subdirectories in the current folder
    items = os.listdir(folder_path)
    num_files_displayed = 0

    for item in items:
        item_path = os.path.join(folder_path, item)

        # If the item is a directory, recursively print its structure
        if os.path.isdir(item_path):
            print_folder_structure(item_path, indent + 1)
        else:
            # If it's a file, print its name with proper indentation
            if num_files_displayed < MAX_FILES_TO_DISPLAY:
                print("  " * (indent + 1) + "|---" + item)
                num_files_displayed += 1
            elif num_files_displayed == MAX_FILES_TO_DISPLAY:
                print("  " * (indent + 1) + "|---...")
                num_files_displayed += 1

        # If there are more than 3 files, print "..." and break the loop
        if num_files_displayed > MAX_FILES_TO_DISPLAY:
            break


# Main function to handle user input and start printing folder structure
def main():
    # Ask user to enter the path of the VSCode project
    project_path = input("Enter the path of the VSCode project: ")

    # Check if the entered path exists
    if os.path.exists(project_path):
        print(f"VSCode Project Structure for: {project_path}")
        # Call the function to print folder and file structure
        print_folder_structure(project_path)
    else:
        print("Invalid project path. Please enter a valid path.")


# Call the main function if the script is run
if __name__ == "__main__":
    main()
