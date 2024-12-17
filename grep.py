import os
import sys
import re

def search_in_file(pattern, filename, ignore_case, show_path=False):
    try:
        flags = re.IGNORECASE if ignore_case else 0
        regex = re.compile(pattern, flags)
        with open(filename, 'r') as file:
            for line in file:
                if regex.search(line):
                    if show_path:
                        print(f"{filename}: {line.strip()}")
                    else:
                        print(line.strip())
    except re.error:
        print("Eroare: Model regex invalid.")
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{filename}' nu a fost găsit.")

def search_in_folder(pattern, path, ignore_case, count, invert_match):
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if count:
                count_pattern_in_file(pattern, file_path, ignore_case, show_path=True)
            elif invert_match:
                search_not_in_file(pattern, file_path, ignore_case, show_path=True)
            else:
                search_in_file(pattern, file_path, ignore_case, show_path=True)

def search_not_in_file(pattern, filename, ignore_case, show_path=False):
    try:
        flags = re.IGNORECASE if ignore_case else 0
        regex = re.compile(pattern, flags)
        with open(filename, 'r') as file:
            line_number = 1
            found = False
            for line in file:
                line_to_check = line.lower() if ignore_case else line
                if not regex.search(line_to_check):
                    if show_path:
                        print(f"{filename}: {line.strip()}")
                    else:
                        print(line.strip())
                    found = True
                line_number += 1
            if not found:
                print(f"{filename}: No unmatched lines found.")
    except re.error:
        print("Error: Invalid regex pattern.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def count_pattern_in_file(pattern, filename, ignore_case, show_path=False):
    try:
        flags = re.IGNORECASE if ignore_case else 0
        regex = re.compile(re.escape(pattern), flags)
        with open(filename, 'r') as file:
            content = file.read()
            match_count = len(regex.findall(content))
        if show_path:
            print(f"{filename}: {match_count}")
        else:
            print(f"{match_count}")
    except re.error:
        print("Error: Invalid regex pattern.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def main():
    if len(sys.argv) < 3:
        sys.exit(1)
    pattern = sys.argv[1]
    path = sys.argv[2]
    ignore_case = False
    count = False
    invert_match = False
    for i, arg in enumerate(sys.argv):
        if arg == '-ignoreCase' and i not in (1, 2):
            ignore_case = True
        if arg == '-count' and i not in (1, 2):
            count = True
        if arg == '-invert-match' and i not in (1, 2):
            invert_match = True

    if os.path.isdir(path):
        search_in_folder(pattern, path, ignore_case, count, invert_match)
    else:
        if os.path.isfile(path):
            if count:
                count_pattern_in_file(pattern, path, ignore_case, show_path=False)
            elif invert_match:
                search_not_in_file(pattern, path, ignore_case, show_path=False)
            else:
                search_in_file(pattern, path, ignore_case, show_path=False)

if __name__ == '__main__':
    main()




