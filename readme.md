# Task Time Tracker

## Summary
This is a task tracker that logs each task in a list, and how long each task took in minutes.

## How to Use
1. Download or clone the repo to your computer
2. Open the cmd line and enter:
   
   ```bash
   python main.py
   ```
3. Follow the prompts in the command line, staring with a name then entering the name of each task you want to add
  -  After entering a task, it asks if you want to add another one. It only accepts yes or no as an input
  -  If no is inputted this way, it proceeds with logging the time spend on each task that was listed
 
## Example
```plaintext
$ python main.py
Enter your name: Alice
Hello Alice. Let's start working!

Enter a task: Write documentation
Would you like to add another task? (yes/no): yes
Enter a task: Review code
Would you like to add another task? (yes/no): no
Let's see how much time you've spent on these tasks:

How long did the Write documentation take to complete? (in minutes): 30
How long did the Review code take to complete? (in minutes): 45

Time spent on tasks:
- Write documentation: 30 minutes
- Review code: 45 minutes

Total time spent on tasks: 75 minutes
Good job, Alice!
```

---

## Other Notes
This is a school project, so it is open-source and can be edited.
