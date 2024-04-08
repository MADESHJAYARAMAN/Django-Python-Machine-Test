import os

def print_directory_structure(root_dir):
    """
    Print the directory structure recursively.
    """
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

def main():
    print("Directory Structure Printer")
    root_dir = os.getcwd()  # Get the current directory
    print_directory_structure(root_dir)

if __name__ == "__main__":
    main()
