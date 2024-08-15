# List of tuples
# Each tuple contains a test case:
# - the first element holds the inputs,
# - the second holds the outputs (including input queries),
# - the third is the message to show in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["4", "4", "4", "4"],
        # Outputs
        ["x1 = ", "y1 = ", "x2 = ", "y2 = ", "distance = 0.00"],
        # Error message
        "Check the variable data types. Check the formula used to measure distance. Make sure the input and output text is identical to the one described in the README.md file"
    ),
    (
        # Inputs
        ["2", "3", "5", "3"],
        # Outputs
        ["x1 = ", "y1 = ", "x2 = ", "y2 = ", "distance = 3.00"],
        # Error message
        "Check the variable data types. Check the formula used to measure distance. Make sure the input and output text is identical to the one described in the README.md file"
    ),
    (
        # Inputs
        ["3", "1", "3", "8"],
        # Outputs
        ["x1 = ", "y1 = ", "x2 = ", "y2 = ", "distance = 7.00"],
        # Error message
        "Check the variable data types. Check the formula used to measure distance. Make sure the input and output text is identical to the one described in the README.md file"
    ),
    (
        # Inputs
        ["2", "-4", "5", "3"],
        # Outputs
        ["x1 = ", "y1 = ", "x2 = ", "y2 = ", "distance = 7.62"],
        # Error message
        "Check the variable data types. Check the formula used to measure distance. Make sure the input and output text is identical to the one described in the README.md file"
    ),
    (
       # Inputs
        ["5", "10" ,"-3", "-4"],
        # Outputs
        ["x1 = ", "y1 = ", "x2 = ", "y2 = ", "distance = 16.12"],
        # Error message
        "Check the variable data types. Check the formula used to measure distance. Make sure the input and output text is identical to the one described in the README.md file"
    ),
]
