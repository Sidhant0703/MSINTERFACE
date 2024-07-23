# Internship Tasks at MSInterface

Welcome to the repository documenting the tasks I completed during my internship at MSInterFace. This repository includes detailed descriptions, code samples, and other relevant information pertaining to the various projects and tasks I worked on.

## Table of Contents

- [Introduction](#introduction)
- [Tasks](#tasks)
  - [Task 1: Implement Caesar Cipher](#task-1-implement-caesar-cipher)
  - [Task 2: Password Complexity Checker](#task-2-password-complexity-checker)
  - [Task 3: Task Name](#task-3-task-name)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This repository contains the tasks and projects I completed during my internship at MSInterface. Each task is documented with descriptions, code snippets, and any other relevant information to help understand the work done and the results achieved.

## Tasks

### Task 1: Implement Caesar Cipher

**Description:**
- The Caesar cipher is a simple encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

**Objective:**
- To create a tool that can encrypt and decrypt text using the Caesar cipher technique.

**Implementation:**

The Caesar cipher implementation involves the following steps:

1. **Importing Prerequisites:**
   - In this case, we do not have any external libraries to import other than Python's built-in `string` module, but it is not necessary for this specific implementation.

2. **Defining the Function:**
   - We define a function `caesar_cipher` that takes three parameters: `text` (the input string), `shift` (the number of positions to shift the letters), and `mode` (either 'encrypt' or 'decrypt').

3. **Encrypting/Decrypting the Text:**
   - The function iterates over each character in the input `text`.
   - For uppercase letters, it shifts the ASCII value within the range of uppercase letters.
   - For lowercase letters, it shifts the ASCII value within the range of lowercase letters.
   - Non-letter characters are added to the result as-is.


4. **Adding ASCII Art:**
   - To give a professional touch to the tool, we add ASCII art displaying "CC-TOOL-KIT" and the author's name.

5. **User Interaction:**
   - The user is prompted to choose whether they want to encrypt or decrypt the text.
   - The user is then asked to enter the text and the shift value.
   - Based on the user's choice, the text is either encrypted or decrypted, and the result is displayed.

**Results:**
![Alt text](Images/caesar_cipher_result.png)

### Task 2: Password Complexity Checker

**Description:**
- This tool checks the complexity of a given password based on multiple criteria, including length, character types, and common passwords. It provides feedback to ensure that the password meets the required security standards.

**Objective:**
- To create a tool that verifies whether a password meets certain complexity requirements to ensure it is secure.

**Implementation:**

The password complexity checker performs the following steps:

1. **ASCII Art Header:**
   - Adds a professional header to the tool.

2. **Defining the Function:**
   - A function `check_password_complexity` checks if the password meets several criteria:
     - Minimum and maximum length.
     - Presence of uppercase letters, lowercase letters, digits, and special characters.
     - Not being a common password or containing common sequences.
     - 
3. **User Interaction:**
   - Prints the ASCII art header.
   - Prompts the user to enter a password and checks its complexity.

**Results:**
![Alt text](Images/pass-checker.png)

### Task 3: Task Name

**Description:**
- Brief description of the task.

**Objective:**
- The main goals and objectives of this task.

**Implementation:**
- Detailed steps and code snippets showing how the task was implemented.

**Results:**
- Any results, screenshots, or output generated from this task.

*(Repeat the above structure for all the tasks completed during the internship)*

## Getting Started

To get a local copy of this project up and running on your machine, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/repositoryname.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd repositoryname
    ```
3. **Install the necessary dependencies:**
    ```bash
    pip install -r requirements.txt  # If using Python
    ```

*(Adjust the steps above according to the specific requirements of your project)*

## Usage

Provide instructions and examples for using the code or accessing the tasks documented in this repository. For example:

```bash
# Example command to run a script
python script_name.py
```

## Acknowledgements

- [MSInterface](https://msinterface.in/)
