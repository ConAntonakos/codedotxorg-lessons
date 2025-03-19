# Introduction to Programming with Python

In this guide, we'll start from scratch and follow a step-by-step approach to learning Python. As developers, we'll use internet searches to solve problems and learn how to approach coding challenges.

## Step 1: Install Python

Before writing any Python code, we need to install Python on our system.

1. **Search for "How to install Python"** on Google or your favorite search engine.
2. Visit the official [Python website](https://www.python.org/downloads/).
3. Download the latest version for your operating system (Windows, macOS, Linux).
4. Install Python, making sure to check the box that says "Add Python to PATH" during the installation process.

### Verification:
1. After installation, open your terminal (or command prompt on Windows).
2. Type `python --version` and press Enter.
3. You should see the version of Python you installed.

## Step 2: Setting Up a Code Editor

A code editor is where you'll write and run your Python code. For this guide, we will use **Visual Studio Code (VSCode)**.

1. **Search for "How to install VSCode"**.
2. Go to the [official VSCode download page](https://code.visualstudio.com/Download) and install it.
3. Once installed, open VSCode and install the **Python extension** by Microsoft.

## Step 3: Write Your First Python Program

Now that we have Python and a code editor set up, let's write your first Python program!

1. Open VSCode and create a new file. Name it `hello.py`.
2. In the file, write the following code:

    ```python
    print("Hello, World!")
    ```

3. **Search for "How to run Python code in VSCode"** if you're unsure how to execute it.
4. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the command palette.
5. Type `Python: Run Python File` and select it.

### Result:
You should see the output `Hello, World!` in the terminal.

## Step 4: Learn Python Syntax

It's time to learn some basic Python syntax. Let's start with variables and data types.

1. **Search for "Python data types"**.
2. Read about basic data types like integers, floats, strings, and booleans.
3. Try the following in your `hello.py` file:

    ```python
    # Variables
    x = 10  # integer
    y = 3.14  # float
    name = "Alice"  # string
    is_active = True  # boolean

    # Print the variables
    print(x)
    print(y)
    print(name)
    print(is_active)
    ```

4. Run the program again to see the outputs.

## Step 5: Learn Control Structures

Control structures like `if` statements and loops help you control the flow of your program.

1. **Search for "Python if statement"** to learn about conditional statements.
2. **Search for "Python for loop"** to learn about loops.

### Example:
```python
# If statement
age = 18
if age >= 18:
    print("You're an adult.")
else:
    print("You're a minor.")

# For loop
for i in range(5):
    print(i)
