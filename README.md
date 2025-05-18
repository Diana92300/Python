# Python Search Utility

A lightweight grep-like tool written in Python for searching text in files and directories.

## Features

* **Search in Files or Folders**

  * Scan a single file or recursively traverse directories.
* **Regular Expression Matching**

  * Supports full Python regex syntax.
* **Optional Flags**

  * `-ignoreCase`: Case-insensitive matching.
  * `-count`: Show the number of matches per file.
  * `-invert-match`: Display lines that **do not** match the pattern.
* **Flexible Output**

  * Print matching lines or file paths with counts.
    
## Examples

* **Search for "TODO" in a single file**:

  ```bash
  python search_tool.py TODO notes.txt
  ```

* **Case-insensitive search for "error" across a directory**:

  ```bash
  python search_tool.py "error" ./logs -ignoreCase
  ```

* **Count occurrences of "import" in a project**:

  ```bash
  python search_tool.py import . -count
  ```

* **Show non-matching lines for pattern `\d+`**:

  ```bash
  python search_tool.py "\d+" data.csv -invert-match
  ```

## Error Handling

* Invalid regex patterns print an error message and exit.
* Missing or invalid file/directory paths are reported to the user.


