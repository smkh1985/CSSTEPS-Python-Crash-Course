# Python for Beginners · CS-Steps

The code for the **Python for Beginners** course on the CS-Steps YouTube channel: every program written in the
videos, and the challenge from the end of each lesson.

## How to use this repository

- **`code/`**: one folder per lesson, with the final version of every file we write in that video.
- **`assignments/`**: the "Your turn" challenge of each lesson.

There's one rule: **don't just watch, code along.** When I type, you type. When a lesson ends with a challenge,
pause the video and try it yourself first; open the code here only to check your work, or when you're stuck.

You need Python 3 and VS Code (lesson 1 sets them up). From lesson 46 on, we use [uv](https://docs.astral.sh/uv/)
for packages: in those folders, run the code with `uv run <file>.py`.

## Lessons

| # | Lesson | Code | Assignment |
|---|---|---|---|
| 1 | Hello, World! Your First Python Program | [code](code/lesson01-hello-world) |  |
| 2 | Variables: Giving Names to Values | [code](code/lesson02-variables) | [assignment](assignments/lesson02-variables.md) |
| 3 | Numbers and Calculations | [code](code/lesson03-numbers) | [assignment](assignments/lesson03-numbers.md) |
| 4 | Strings: Working with Text | [code](code/lesson04-strings) | [assignment](assignments/lesson04-strings.md) |
| 5 | Lists: Store and Access Multiple Values | [code](code/lesson05-lists) | [assignment](assignments/lesson05-lists.md) |
| 6 | User Input and List Operations | [code](code/lesson06-input-lists) | [assignment](assignments/lesson06-input-lists.md) |
| 7 | Lists: Negative Indexes and Slicing | [code](code/lesson07-slicing) | [assignment](assignments/lesson07-slicing.md) |
| 8 | Looping Through a List with for | [code](code/lesson08-for-loops) | [assignment](assignments/lesson08-for-loops.md) |
| 9 | Making Numerical Lists with range() | [code](code/lesson09-numerical-lists) | [assignment](assignments/lesson09-numerical-lists.md) |
| 10 | Copying a List (and the Surprise You Need to Know) | [code](code/lesson10-copying-lists) | [assignment](assignments/lesson10-copying-lists.md) |
| 11 | Tuples: Collections That Don't Change | [code](code/lesson11-tuples) | [assignment](assignments/lesson11-tuples.md) |
| 12 | More List Tools: len, in, count, index, sort and more | [code](code/lesson12-list-methods) | [assignment](assignments/lesson12-list-methods.md) |
| 13 | Looping with enumerate() and zip() | [code](code/lesson13-enumerate-zip) | [assignment](assignments/lesson13-enumerate-zip.md) |
| 14 | Booleans and Conditional Tests | [code](code/lesson14-conditional-tests) | [assignment](assignments/lesson14-conditional-tests.md) |
| 15 | The if Statement | [code](code/lesson15-if) | [assignment](assignments/lesson15-if.md) |
| 16 | else and elif | [code](code/lesson16-else-elif) | [assignment](assignments/lesson16-else-elif.md) |
| 17 | Combining Conditions: and, or, not | [code](code/lesson17-and-or-not) | [assignment](assignments/lesson17-and-or-not.md) |
| 18 | List Comprehensions with if | [code](code/lesson18-comprehension-if) | [assignment](assignments/lesson18-comprehension-if.md) |
| 19 | Dictionaries: Key-Value Pairs | [code](code/lesson19-dictionaries) | [assignment](assignments/lesson19-dictionaries.md) |
| 20 | Changing a Dictionary: Add, Update, Delete, Combine | [code](code/lesson20-dict-changes) | [assignment](assignments/lesson20-dict-changes.md) |
| 21 | Looping Over a Dictionary: keys(), values(), items() | [code](code/lesson21-dict-loops) | [assignment](assignments/lesson21-dict-loops.md) |
| 22 | lesson22-get-dict-comprehension | [code](code/lesson22-get-dict-comprehension) | [assignment](assignments/lesson22-get-dict-comprehension.md) |
| 23 | The while Loop | [code](code/lesson23-while-loops) | [assignment](assignments/lesson23-while-loops.md) |
| 24 | Functions | [code](code/lesson24-functions) | [assignment](assignments/lesson24-functions.md) |
| 25 | Parameters, Arguments and return | [code](code/lesson25-parameters-return) | [assignment](assignments/lesson25-parameters-return.md) |
| 26 | Default Parameter Values | [code](code/lesson26-default-values) | [assignment](assignments/lesson26-default-values.md) |
| 27 | *args and **kwargs | [code](code/lesson27-args-kwargs) | [assignment](assignments/lesson27-args-kwargs.md) |
| 28 | Unpacking Arguments with * and ** | [code](code/lesson28-unpacking) | [assignment](assignments/lesson28-unpacking.md) |
| 29 | Returning Multiple Values | [code](code/lesson29-return-tuple) | [assignment](assignments/lesson29-return-tuple.md) |
| 30 | Passing a List to a Function | [code](code/lesson30-list-arguments) | [assignment](assignments/lesson30-list-arguments.md) |
| 31 | Modules: Storing Functions in Files | [code](code/lesson31-modules) | [assignment](assignments/lesson31-modules.md) |
| 32 | What Is an Object? (OOP Concepts) | (no code: ideas only) | [assignment](assignments/lesson32-objects.md) |
| 33 | Your First Class: __init__, self and Objects | [code](code/lesson33-classes) | [assignment](assignments/lesson33-classes.md) |
| 34 | A Grade Book Class: Attributes, a Dictionary and Methods | [code](code/lesson34-grade-book) | [assignment](assignments/lesson34-grade-book.md) |
| 35 | __str__ and __repr__: Printing Your Objects | [code](code/lesson35-str-method) | [assignment](assignments/lesson35-str-method.md) |
| 36 | Inheritance: super() and Overriding Methods | [code](code/lesson36-inheritance) | [assignment](assignments/lesson36-inheritance.md) |
| 37 | Class Variables vs Instance Variables | [code](code/lesson37-class-variables) | [assignment](assignments/lesson37-class-variables.md) |
| 38 | The random Module: A Guessing Game and a Prize Wheel | [code](code/lesson38-random) | [assignment](assignments/lesson38-random.md) |
| 39 | Dataclasses: Less Code for Classes That Hold Data | [code](code/lesson39-dataclasses) | [assignment](assignments/lesson39-dataclasses.md) |
| 40 | Saving Data in Files: Plain Text, CSV and JSON | [code](code/lesson40-data-files) | [assignment](assignments/lesson40-data-files.md) |
| 41 | Reading and Writing JSON Files in Python | [code](code/lesson41-json-files) | [assignment](assignments/lesson41-json-files.md) |
| 42 | Saving Objects in JSON: to_dict and from_dict | [code](code/lesson42-objects-json) | [assignment](assignments/lesson42-objects-json.md) |
| 43 | Errors and raise: Python's Errors and Your Own | [code](code/lesson43-errors-raise) | [assignment](assignments/lesson43-errors-raise.md) |
| 44 | try, except, else, finally: Handling Errors in Python | [code](code/lesson44-try-except) | [assignment](assignments/lesson44-try-except.md) |
| 46 | Virtual Environments and uv: Installing Python Packages | [code](code/lesson46-virtual-env) | [assignment](assignments/lesson46-virtual-env.md) |
| 47 | Testing Your Code by Hand (and Why It Isn't Enough) | [code](code/lesson47-manual-testing) | [assignment](assignments/lesson47-manual-testing.md) |
| 48 | Automated Tests with pytest | [code](code/lesson48-pytest) | [assignment](assignments/lesson48-pytest.md) |
