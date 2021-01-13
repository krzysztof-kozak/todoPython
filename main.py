class ToDo:
    def __init__(self, title: str):
        self.title = title
        self.is_completed = False

    def show_todo(self):
        if self.is_completed:
            emoji = '✔'
        else:
            emoji = '❌'

        return f'{self.title}: {emoji}'


class ToDoApp:
    def __init__(self):
        self.todos = []

    def start_application(self):
        self.get_user_input()

    def get_user_input(self):
        while True:
            print(
                f'\n{"*" * 50}\n\nWhat would you like to do with your list? Type "show", "add", "complete", "remove", "quit"'
            )
            user_action = input('I\'d like to: ')

            self.process_user_action(user_action)

    def process_user_action(self, user_action):
        if user_action == 'show':
            self.get_todos()
        elif user_action == "add":
            self.verify_user_input()
        elif user_action == "complete":
            self.toggle_complete()
        elif user_action == "remove":
            self.remove_todo()
        elif user_action == "quit":
            quit(0)
        else:
            print('Sorry, I don\'t understand')

    def verify_user_input(self):
        is_user_input_correct = False

        while not is_user_input_correct:
            user_input = input("Enter your todo: ")
            if len(user_input) > 3:
                is_user_input_correct = True
                self.add_todo(user_input)
            else:
                print("Your todo must be at least 4 characters")

    def verify_task_number(self, task_number):
        list_size = len(self.todos)

        if task_number == "cancel":
            return False

        if not task_number.isdigit():
            print(
                f'\n{"*" * 50}\n\n{task_number} is not a valid task number.\n')
            return False

        if int(task_number) < 1 or int(task_number) > list_size:
            print(f'\n{"*" * 50}\n\nThis number is out of scope.\n')
            return False

        return True

    def check_if_list_is_empty(self):
        if not self.todos:
            print("The task list is empty")
            return True

        return

    def add_todo(self, verified_user_input):
        self.todos.append(ToDo(verified_user_input))

    def remove_todo(self):
        print("Here are your current tasks: \n \n")
        self.get_todos()

        task_number = input(
            "\nType the number of the task to remove (or type cancel to leave): "
        )
        if not self.verify_task_number(task_number):
            return

        self.todos.pop(int(task_number) - 1)

        print(
            f'\n{"*" * 50}\n\nI have removed the task number {task_number}\n')
        print("Here is an updated task list: \n")
        self.get_todos()

    def toggle_complete(self):
        if self.check_if_list_is_empty():
            return

        print("Here are your current tasks: \n")
        self.get_todos()

        task_number = input(
            "\nType the number of the task to toggle complete (or type cancel to leave): "
        )
        if not self.verify_task_number(task_number):
            return

        self.todos[int(task_number) - 1].is_completed = not self.todos[
            int(task_number) - 1].is_completed

        print(f'\n{"*" * 50}\n\nI have completed the task!\n')
        self.get_todos()

    def get_todos(self):
        if self.check_if_list_is_empty():
            return

        for index, todo in enumerate(self.todos):
            print(f'{index+1}. {todo.show_todo()}.')


my_todo_app = ToDoApp()
my_todo_app.start_application()
