import os
import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="A script with -c and -l options")
    
    # Add the -c argument
    parser.add_argument('-c', '--code', action='store_true', help='code')
    
    # Add the -l argument
    parser.add_argument('-l', '--list', action='store_true', help='list')

    # Add the -w argument
    parser.add_argument('-w', '--word', action='store_true', help='Words')

    #Add the -m argument
    parser.add_argument('-m', '--many', action='store_true', help='characters')

    # Parse the arguments
    args = parser.parse_args()

    # Define the file
    file = "test.txt"

    # Print "hello world" if -l option is provided and exit
    if args.list:
        with open(file, 'r') as f:
            line_count = sum(1 for line in f)
        print(f"Number of lines in '{file}': {line_count}")
        return

    # Check if the file exists
    if not os.path.exists(file):
        print(f"File '{file}' does not exist.")
        return

    # Get the file size
    file_size = os.stat(file)

    # Print the file size
    print(f"File size of '{file}': {file_size.st_size} bytes")

    # Execute the specific part of the code if -c option is provided
    if args.code:
        print("The -c option was provided, executing the specific part of the code.")
        specific_function()

    if args.word:
        number_of_words = 0
        with open(r'test.txt', 'r') as file:
            data = file.read()
            lines = data.split()
            number_of_words += len(lines)
        print(number_of_words)

    if args.many:
        with open(file, 'r')as file:
            content = file.read()
        number_of_characters = len(content)
        print(number_of_characters)
        


def specific_function():
    print("Executing the specific function!")

if __name__ == "__main__":
    main()
