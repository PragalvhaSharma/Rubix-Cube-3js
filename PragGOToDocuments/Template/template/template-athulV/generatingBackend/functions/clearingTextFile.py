
def clear_file_if_not_empty(file_path):
    """
    Clears the content of the file if it is not empty.

    Parameters:
    file_path (str): Path to the file to be checked and cleared.
    """
    with open(file_path, "r") as file:
        content = file.read()
        if content.strip():  # Check if the file content is not empty or just whitespace
            with open(file_path, 'w') as file_to_clear:
                file_to_clear.write("")

# Example usage
# file_path = "path/to/your/file.txt"
# clear_file_if_not_empty(file_path)