import operator

# Include standard module
def include_standard_module():
    # Placeholder for including standard module
    pass

# Execute main part of the code
def execute_main(lines):
    # Variable declaration
    variables = {}

    # Iterate over each line of code
    for line in lines:
        parts = line.strip().split()

        # Check for main execution block
        if parts[0] == "cover" and parts[1] == "(" and parts[2] == ")" and parts[3] == ";":
            continue  # Skip cover statement
        
        # Check for variable declaration
        if parts[0] == "set":
            for var_name in parts[1:]:
                if var_name != "as":
                    variables[var_name] = None

        # Check for user input
        elif parts[0] == "ask":
            try:
                var_name = parts[-1][:-1]
                user_input = input(parts[1][1:-2])
                variables[var_name] = int(user_input)
            except ValueError:
                print("Error: Invalid input. Please enter an integer value.")

        # Check for arithmetic operation
        elif parts[0] == "add":
            try:
                print("Before addition:", variables)
                var1 = variables[parts[1]]
                var2 = variables[parts[3]]
                result = operator.add(var1, var2)
                variables[parts[-1]] = result
                print("After addition:", variables)
            except KeyError:
                print("Error: Variable not declared.")

        # Check for output
        elif parts[0] == "show":
            try:
                print("Result:", variables[parts[1]])
            except KeyError:
                print("Error: Variable not declared.")

# Main function
def main():
    # Read code from file
    try:
        with open("program.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: File 'program.txt' not found.")
        return

    # Check for standard module inclusion
    if lines and lines[0].strip() == "@take smod!":
        include_standard_module()
        # Remove the first line from the code
        lines = lines[1:]

    # Execute main part of the code
    execute_main(lines)

# Entry point
if __name__ == "__main__":
    main()
