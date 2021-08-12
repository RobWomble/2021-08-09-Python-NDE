# Create a function that will accept a list of integers AS AN ARGUMENT that will then grade each integer like a test (A > 90, B > 80 ...). Count the number of A's, B's, C's, D's, and F's, then return a dictionary in the format:    {"A": 3, "B": 7, ... }


def grader(grades):
    print(grades)
    a = 0 
    b = 0
    c = 0
    d = 0
    f = 0
    final_scores = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades:
        print(grade)
        if grade > 89:
            a += 1
            final_scores["A"] += 1
            # final_scores["A"] = final_scores["A"] + 1
        elif grade > 79:
            final_scores["B"] += 1
        elif grade > 69:
            final_scores["C"] += 1
        elif grade > 59:
            final_scores["D"] += 1
        else:
            final_scores["F"] += 1
    result = {"A": a, "B": b, "C": c, "D": d, "F": f}
    return final_scores


# dict_name["key"] = "new value"
def main():
    nums = input("What numbers do you want to get graded? ").split()
    int_nums = [int(n) for n in nums] 
    #int_nums = []
    #for n in nums:
    #    int_nums.append(int(n))
    print(grader(int_nums))
    

main()
#scores = [11, 101, 99, 5, 78, 93, 84, 66]
#print(grader(scores))
