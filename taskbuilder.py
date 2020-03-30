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
        self._get_and_set_name()
        self._get_and_set_hours()
        self._get_and_set_priority()

    # methods to get and set attributes
    def _get_and_set_name(self):
        name = input('Enter name for this task: ')
        self.name = name.capitalize()

    def _get_and_set_start_time(self):
        pass

    def _get_and_set_end_time(self):
        pass

    def _get_and_set_hours(self):
        hours = input('Enter number of hours this task needs: ')
        try:
            self.hours = float(hours)
        except ValueError:
            self._get_and_set_hours()

    def _get_and_set_priority(self):
        priority = input('Enter task priority: ')
        try:
            priority = int(priority)
            if priority < 0 or priority > 4:
                self._get_and_set_priority()
            else:
                self.priority = priority
        except ValueError:
            self._get_and_set_priority()

    # methods to set attributes, these may be chained together
    # as of now there is no error checking, if you call this method
    # it is assumed that the input is valid
    def set_flexibility(self, flexibility: bool):
        self.flexible = flexibility
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def set_begin(self):
        pass

    def set_end(self):
        pass

    def set_hours(self, hours: float):
        self.hours = hours
        return self

    def set_priority(self, priority: int):
        self.priority = priority
        return self

    def build(self):
        """Builds the current configuration of Task and returns it"""
        ret = Task(self.name, self.begin, self.end, self.priority, self.hours)
        self.reset()  # resets the current configuration
        return ret

    def reset(self):
        """Resets the attributes for building the next Task"""
        self.__init__()


if __name__ == '__main__':
    builder = TaskBuilder()
    # builder.get_data_from_input()
    # task = builder.build()
    # print(task)
    builder.set_flexibility(False).set_priority(0).set_hours(3.5).set_name('testTask')
    task2 = builder.build()
    print(task2)
