def process_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            content = file.readlines()  # Read all lines into a list
        
        # Count the number of lines, words, and characters
        num_lines = len(content)
        num_words = sum(len(line.split()) for line in content)
        num_chars = sum(len(line) for line in content)
        
        # Prepare the result string
        result = (
            f"File Analysis:\n"
            f"Number of lines: {num_lines}\n"
            f"Number of words: {num_words}\n"
            f"Number of characters: {num_chars}\n"
        )
        
        # Write the result to the output file
        with open(output_file, 'w') as file:
            file.write(result)
        
        print("File processed successfully. Results written to the output file.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_file = "input.txt"   # Replace with your input file path
output_file = "output.txt" # Replace with your desired output file path
process_file(input_file, output_file)



'''
Logic Explanation:
Read the Input File:

The script uses open() in read mode ('r') to read the contents of the input file.
readlines() reads the file line by line into a list, where each list element is a line from the file.
Count Lines:

The number of lines is simply the length of the list (len(content)).
Count Words:

Each line is split into words using line.split().
The total number of words is the sum of the lengths of these split lists.
Count Characters:

The len(line) function is applied to each line to count the characters, including spaces and newlines.
These counts are summed up for all lines.
Write to the Output File:

The open() function with write mode ('w') is used to create or overwrite the output file.
The program writes a formatted summary of the analysis to this file.
Error Handling:

If the input file doesn’t exist, a FileNotFoundError is caught, and a friendly error message is displayed.
A generic Exception block catches unexpected errors.
How to Test This Script:
Create a text file named input.txt (or any other name you choose) with some sample text.
Update the input_file and output_file variables in the script with the respective file names.
Run the script. Check the contents of output.txt to see the analysis.
'''