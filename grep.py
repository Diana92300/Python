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

    if os.path.isfile(path):
            search_in_file(pattern, path, ignore_case, show_path=False)

if __name__ == '__main__':
    main()
