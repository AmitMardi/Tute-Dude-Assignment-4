# Task 1: Read a File and Handle Errors

This Python program attempts to read the first two lines of a file named `sample.txt` and display them.  
If the file is not found, it displays an error message instead of crashing.

## How to Use

1. Make sure a file named `sample.txt` exists in the same directory as the program.
2. Run the program.
3. The program will:
   - Read and display the first two lines of the file.
   - Show an error message if the file does not exist.

**Note:**  
- `strip()` is used to remove extra spaces or newline characters from the read lines.  
- The program uses a `try-except` block to handle missing file errors.


# Task 2: Write and Append Data to a File

This Python program allows the user to:
1. Write text to a file named `output.txt` (overwriting any existing content).
2. Append additional text to the same file.
3. Read and display the final content of the file.

## How to Use

1. Run the program.
2. Enter text when prompted to write to the file.
3. Enter additional text when prompted to append to the file.
4. The program will:
   - Save both entries to `output.txt`.
   - Display the final content of the file.

**Note:**  
- Writing (`"w"`) mode will erase previous content in the file.  
- Appending (`"a"`) mode adds new text without removing existing content.
