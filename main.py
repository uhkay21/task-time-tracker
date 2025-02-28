user = input("Enter your name: ")
tasks = []
task_time = []

print(f"Hello {user}. Let's start working!")

while True:
    task_name = input("Enter a task: ")
    tasks.append(task_name)
    while True:
        add_more = input("Would you like to add another task? (yes/no): ").lower()
        if add_more in ['yes', 'no']:
            break
        else:
            print(f"Please enter yes or no.")
    if add_more == 'no':
        print(f"Let's see how much time you've spent on these tasks:")
        break

for task in tasks:
    while True:
        try:
            time_spent = int(input(f"How long did the {task} take to complete? (in minutes): "))
            task_time.append(time_spent)
            break
        except ValueError:
            print("Please enter a valid number.")

print("\nTime spent on tasks:")
for task, time in zip(tasks, task_time):
    print(f"- {task}: {time} minutes")

print("\nTotal time spent on tasks:", sum(task_time), "minutes")
print(f"Good job, {user}!")