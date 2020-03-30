from task import Task


class TaskBuilder:
    """
    This class handles the creation of Task objects.
    """

    def __init__(self):
        self.flexible = True
        self.name = None
        self.begin = None
        self.end = None
        self.hours = None
        self.priority = None

    def get_data_from_input(self):
        self.get_and_set_name()
        self.get_and_set_hours()
        self.get_and_set_priority()

    def get_and_set_name(self):
        name = input('Enter name for this task: ')
        self.name = name.capitalize()

    def get_and_set_start_time(self):
        pass

    def get_and_set_end_time(self):
        pass

    def get_and_set_hours(self):
        hours = input('Enter number of hours this task needs: ')
        try:
            self.hours = float(hours)
        except ValueError:
            self.get_and_set_hours()

    def get_and_set_priority(self):
        priority = input('Enter task priority: ')
        try:
            priority = int(priority)
            if priority < 0 or priority > 4:
                self.get_and_set_priority()
            else:
                self.priority = priority
        except ValueError:
            self.get_and_set_priority()

    def build(self):
        """Builds the current configuration of Task and returns it"""
        task = Task(self.name, self.begin, self.end, self.priority, self.hours)
        self.reset()  # resets the current configuration
        return task

    def reset(self):
        """Resets the attributes for building the next Task"""
        self.__init__()


if __name__ == '__main__':
    builder = TaskBuilder()
    builder.get_data_from_input()
    task = builder.build()
    print(task)
