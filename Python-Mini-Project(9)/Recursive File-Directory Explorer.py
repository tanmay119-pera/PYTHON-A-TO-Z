'''                               PROJECT 9 - Recursive File/Directory Explorer

This program uses RECURSION (a function calling itself) to look Inside a folder, and every folder inside that 
folder, and so on - then prints everything as a neat indented tree.

Recursion Concepts Demonstrated:

1. Base Case      -> when to STOP recursing (invalid path / no permission)

2. Recursive Case -> the function calling ITSELF to go one level deeper

3. Returning values from recursive calls (to count files & folders)

Module Used: os (built-in Python module, no installation needed) It lets us talk to the file system - list folders,
check if something is a file/folder, get file size, etc.'''

import os  # os = "operating system" module, gives us file/folder tools
def explore_directory(path, depth=0):

    '''Recursively explores path and prints its structure.

Parameters:
path (str)  -> the folder we want to look inside
depth (int) -> how many levels deep we currently are. We use this only to add indentation (spaces) so nested
items look like a tree.

Returns:
(file_count, folder_count) -> total files & folders found inside this path (including everything inside sub-folders)'''

# ----------- BASE CASE -----------
# A base case is what STOPS the recursion. Without one, the
# function would keep calling itself forever and crash.
# Here: if 'path' is not a real folder, we stop immediately.

    if not os.path.isdir(path):
        # os.path.isdir() returns True only if 'path' is a folder

        print("  " * depth + f"[Not a valid directory] {path}")
        return 0, 0   # nothing found, so 0 files and 0 folders

    # try/except is used because listing a folder can sometimes fail
    # (e.g. a protected system folder we're not allowed to open).
    # "try" = attempt this code, "except" = do this instead if it fails.

    try:
        items = sorted(os.listdir(path))

        # os.listdir(path) -> gives us a list of names (files + folders)
        #                      that are directly inside 'path'
        # sorted(...)       -> just arranges them alphabetically

    except PermissionError:
        print("  " * depth + f"[Permission Denied] {path}")
        return 0, 0

    # These two variables will keep count of what we find in THIS folder
    # (including everything inside any sub-folders we recurse into)

    file_count = 0
    folder_count = 0

    # Loop through every name we found inside this folder
    for item in items:

        # os.path.join() safely combines a folder path + item name
        # e.g. join("myfolder", "notes.txt") -> "myfolder/notes.txt"

        item_path = os.path.join(path, item)

        # "  " * depth just repeats two spaces 'depth' times,
        # so items that are deeper get printed further to the right

        indent = "  " * depth

        if os.path.isdir(item_path):

            # ---- This item is a FOLDER ----

            print(f"{indent}📁 {item}/")
            folder_count += 1   # count this folder

            # ----------- RECURSIVE CASE -----------
            # This is the key recursion step: the function calls
            # ITSELF, but on the sub-folder, and one level deeper
            # (depth + 1). It keeps happening until the base case
            # (an empty or inaccessible folder) is reached.
            f, d = explore_directory(item_path, depth + 1)

            # Add whatever the recursive call found to our own totals
            file_count += f
            folder_count += d
        else:

            # ---- This item is a FILE ----

            size = os.path.getsize(item_path)   # size of file in bytes
            print(f"{indent}📄 {item} ({size} bytes)")
            file_count += 1   # count this file

# Send our totals back up to whoever called this function
# (either main(), or an earlier/parent call to explore_directory)
    return file_count, folder_count


def main():

    # input() shows a message and waits for the user to type something
    # .strip() removes any accidental extra spaces at the start/end

    folder_path = input("Enter folder path to explore (press Enter for current folder): ").strip()

    if folder_path == "":
        folder_path = "."   # "." is a shortcut meaning "current folder"

    # os.path.abspath() turns "." into the full, readable folder path
    print(f"\nExploring: {os.path.abspath(folder_path)}\n" + "-" * 40)

    # This is the FIRST call that kicks off the whole recursion chain
    total_files, total_folders = explore_directory(folder_path)

    print("-" * 40)
    print(f"Total Files   : {total_files}")
    print(f"Total Folders : {total_folders}")


# This checks if the file is being run directly (not imported elsewhere)
# It's a standard Python convention for the "start point" of a script
if __name__ == "__main__":
    main()