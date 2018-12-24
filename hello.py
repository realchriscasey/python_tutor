"""
EXAMPLE CODE for argument parsing in Python

Shows how to read and utilize command line arguments in Python.
"""

# python argparse module can parse arguments and provides basic command line 
# help functionality. See: https://docs.python.org/3/library/argparse.html
import argparse


"""
Placing argument parsing at the top of the script provides the reader a
good overview of what the script is for.
"""

def parse_args():
    # create a parser object and give a description of your program's function
    parser = argparse.ArgumentParser(description='Greet the Universe.')

    # add an argument to the parser, including the argument name, its
    # description, and optionally a default value
    # note that args a hyphen '-' will map to variables with an underscore '_'
    parser.add_argument('--the-universe', default='world',
                    help='Name your universe')
    
    # parse the command line input
    args = parser.parse_args()

    # you can also modify arguments after they've been read.
    args.the_universe = args.the_universe.capitalize() 

    return args


"""
The use of a main() function is one way to highlight the script entrypoint
As a bonus, you can safely reference functions that aren't yet defined.

This main method accepts the 'args' result that 

Note: the function "main" has no implicit handling or special meaning.
Later on we will call it explicitly.
"""

def main(args):
    # read the argument value that was set earlier
    greeting_target = args.the_universe
    greet(greeting_target)


"""
after argument parsing and main function, include supporting functions
"""

# send a greeting to <target> 
def greet(target):
    print("Hello {universe}".format(universe=target))


"""
by convention (and to ensure that all functions have been defined), we
execute the main function as the very last line in the script.

this is where we use python's __name__ attribute to determine if the script
is being executed (vs. being imported as a module elsewhere).
"""

if __name__ == "__main__":
    # call parse_args() and pass the resulting argument object to main()
    main(parse_args())


"""
Errata:

To create new command line arguments in Visual Studio Code, do the following:
1) In the Debug menu, click 'Open Configurations'
2) Find the Configuration you wish to edit
   (The default configuration may be called "Python: Current File (Integrated Terminal)")
3) add a field called "args" containing an array of strings with the arguments you with to include
4) save 'launch.json' and run from the debugger

Example launch.json:
{
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Python: Current File (Integrated Terminal)",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": ["--the-universe=\"Dumbledore\""]
        }
}
"""