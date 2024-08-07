import os
import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="A script with -c and -l options")
    
    # Add the -c argument
    parser.add_argument('-c', '--code', action='store_true', help='Execute the specific part of the code')
    
    # Add the -l argument
    parser.add_argument('-l', '--list', action='store_true', help='Print "hello world"')

    # Parse the arguments
    args = parser.parse_args()

    # Print "hello world" if -l option is provided and exit
    if args.list:
        print_hello_world()
        return

    # Define the file
    file = "test.txt"

    # Check if the file exists
    if not os.path.exists(file):
        print(f"File '{file}' does not exist.")
        return

    # Get the file size
    file_size = os.stat(file)

    # Print the file size
    print({file_size.st_size})

    # Execute the specific part of the code if -c option is provided
    if args.code:
        print("The -c option was provided, executing the specific part of the code.")
        specific_function()

def specific_function():
    print("Executing the specific function!")

def print_hello_world():
    print("Hello World")

if __name__ == "__main__":
    main()
