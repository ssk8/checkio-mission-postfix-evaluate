"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[2, 3, '+', 4, '*']],
            "answer": 20,
        },
        {
            "input": [[2, 3, 4, '*', '+']],
            "answer": 14,
        },
        {
            "input": [[3, 3, 3, '-', '/', 42, '+']],
            "answer": 42,
        },
    ],
    "Extra": [
        {
            "input": [[7, 3, '/']],
            "answer": 2,
        },
        {
            "input": [[5, 2, "-"]],
            "answer": 3,
        },
        {
            "input": [[1, 2, 3, 4, 5, '*', '*', '*', '*']],
            "answer": 120,
        },
    ]
}
