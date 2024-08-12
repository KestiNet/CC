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

    # Add the -m argument
    parser.add_argument('-m', '--many', action='store_true', help='characters')

    # Add the -i argument
    parser.add_argument('-i', '--iterate', action='store_true', help='iterate')

    # Parse the arguments
    args = parser.parse_args()

    # Define the file
    filename = "test.txt"

    # If no flags are provided, default to -c, -l, and -w
    if not any([args.code, args.list, args.word, args.many, args.iterate]):
        args.code = True
        args.list = True
        args.word = True

    if args.iterate:
        # Print all arguments and their values
        print("Arguments provided:")
        for arg in vars(args):
            print(f"{arg}: {getattr(args, arg)}")

    # Execute the specific part of the code if -c option is provided
    if args.code:
        print("The -c option was provided, executing the specific part of the code.")
        specific_function()

    # Print the number of lines if -l option is provided
    if args.list:
        with open(filename, 'r') as f:
            line_count = sum(1 for line in f)
        print(f"Number of lines in '{filename}': {line_count}")

    # Print the number of words if -w option is provided
    if args.word:
        number_of_words = 0
        with open(filename, 'r') as file_obj:
            data = file_obj.read()
            lines = data.split()
            number_of_words += len(lines)
        print(f"Number of words in '{filename}': {number_of_words}")

    # Print the number of characters if -m option is provided
    if args.many:
        with open(filename, 'r') as file_obj:
            content = file_obj.read()
        number_of_characters = len(content)
        print(f"Number of characters in '{filename}': {number_of_characters}")

    # Check if the file exists
    if not os.path.exists(filename):
        print(f"File '{filename}' does not exist.")
        return


def specific_function():
    print("Executing the specific function!")

if __name__ == "__main__":
    main()
