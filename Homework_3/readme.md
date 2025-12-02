### **Task: Write a Simple Shell Script**

#### **Goal**

Create a simple shell script to practice basic shell scripting commands such as `echo`, variables, and functions.

---

### **What You Need to Do**

1. **Create a new shell script file** named `simple_script.sh`.
   Example:

   ```bash
   nano simple_script.sh
   ```

2. **Inside the script**, you must:

   * Add the **shebang line** (`#!/bin/bash`) at the top.
   * Use `echo` commands to print messages to the terminal.
   * Create at least **one variable** (for example, a name) and display it using `echo`.
   * Write a simple **function** that prints at least two lines of text.
   * Call the function in your script.
   * Create another variable (for example, the current date using `date`) and display it.
   * Change one of your variables and print the new value.

3. **Make the script executable** using:

   ```bash
   chmod +x simple_script.sh
   ```

4. **Run the script** to check that everything works:

   ```bash
   ./simple_script.sh
   ```

---
Sure! Here’s a short note you can include in your task or notes section 👇

---

### **Notes**

#### **Assigning a Command Result to a Variable**

You can save the result of a command into a variable using **command substitution** — either with backticks (`` ` ``) or with `$( )` (recommended).

**Example:**

```bash
CURRENT_DATE=$(date)
```

This runs the `date` command and stores its output in the variable `CURRENT_DATE`.
You can then display it using:

```bash
echo "Today is: $CURRENT_DATE"
```

---

#### **About the `date` Command**

The `date` command is used to display or set the system date and time.
By default, it shows the current date and time, for example:

```
Sun Nov  3 16:25:12 EET 2025
```

You can also format the output. For example:

```bash
date "+%Y-%m-%d %H:%M:%S"
```

This would print:

```
2025-11-03 16:25:12
```
