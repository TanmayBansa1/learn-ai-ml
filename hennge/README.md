# HENNGE Admission Challenge Solutions

This repository contains the solution for the HENNGE Admission Challenge for backend positions and global internship applicants.

## Mission 1: Power of Four of Negative Integers

The solution for Mission 1 is implemented in Python (`main.py`), following all the specified constraints.

### Problem Description

- The input will be a list of integers, each separated by a newline character.
- The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
- Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
- For each test case, calculate the power of four of Yn, excluding when Yn is positive, and print the calculated sum in the output.
- If X and the number of integers Yn are not equal, print -1 as the output.

### Rules
- No use of for loops, while loops, or list/set/dictionary comprehensions.
- All operations must be implemented using recursion.
- No global variables.
- Solution must be in a single file.

### Running the Python Solution

```bash
python main.py
```

### Example

Input:
```
2
4
3 -1 1 10
5
9 -5 -5 -10 10
```

Output:
```
1
11250
```

### How it Works

1. First test case: 3 -1 1 10
   - Only include negative numbers: -1
   - Power of four: (-1)^4 = 1
   - Sum: 1

2. Second test case: 9 -5 -5 -10 10
   - Only include negative numbers: -5, -5, -10
   - Powers of four: (-5)^4 + (-5)^4 + (-10)^4 = 625 + 625 + 10000 = 11250
   - Sum: 11250

## Mission 2: Publish as a Secret Gist

After completing Mission 1, you need to publish your solution as a secret GitHub gist:

1. Create a GitHub account if you don't have one
2. Visit https://gist.github.com/
3. Upload your solution file as `main.py`
4. Make sure to set it as a "Secret gist" (not public)
5. Save the URL to your gist for Mission 3

## Mission 3: Submit Your Solution

The `mission3.py` script helps you submit your solution to the HENNGE API with the required TOTP authentication.

### Prerequisites

Install the required Python packages:

```bash
pip install requests
```

### Usage

```bash
python mission3.py <your_email> <github_gist_url> [language]
```

Replace:
- `<your_email>` with your email address
- `<github_gist_url>` with the URL to your secret gist from Mission 2
- `[language]` (optional) with "python" (default) or "golang"

### How it Works

The script:
1. Constructs a JSON payload with your email, GitHub gist URL, and solution language
2. Generates a TOTP (Time-based One-Time Password) according to RFC6238
3. Uses HTTP Basic Authentication with your email and TOTP
4. Makes a POST request to the HENNGE API
5. Displays the response from the server

If successful, you'll receive a 200 status code with a congratulatory message.

## Notes

- The TOTP implementation uses HMAC-SHA-512 as specified in the challenge
- The shared secret is constructed by appending "HENNGECHALLENGE004" to your email
- The time step for TOTP is 30 seconds
- The TOTP code is 10 digits long 