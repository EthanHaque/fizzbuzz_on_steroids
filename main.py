"""
Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” 
instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.
"""


def simple_solution():
    """
    Simple solution to fizzbuzz.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def more_complex_solution():
    """
    A slightly more complex solution.
    """
    for i in range(1, 101):
        out = ""
        if i % 3 == 0:
            out += "Fizz"
        if i % 5 == 0:
            out += "Buzz"
        if out == "":
            out += str(i)
        print(out)

# def even_more_complex_solution():
#     mod_dict = {3: "Fizz", 5: "Buzz"}
#     for i in range(1, 101):
#         out = ""


if __name__ == "__main__":
    more_complex_solution()
