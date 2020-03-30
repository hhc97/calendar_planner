from datetime import datetime, timedelta


class Task:
    """
    Args:
        name(str): the name of the task
        begin(datetime, or str): the begin time of the task.
                If it is str, it is in "09/19/18 13:55:26" format.
                If begin is given, the task's flexibility is set to False and
                priority set to 4.
        end(datetime, or str): the end time of the task. Same format as begin.
        priority (int): a value in [0, 1, 2, 3, 4].
        hours (float): will be rounded to the nearest 0.5
    """

    def __init__(self, name, begin=None, end=None, priority=0, hours=1.0):
        self.flexible = True
        self.name = name
        self.begin = None
        self.end = None
        self.hours = round(2 * hours) / 2
        self.priority = priority

        if begin is not None:
            if not isinstance(begin, datetime):
                begin = datetime.strptime(begin, '%m/%d/%y %H:%M:%S')
            self.begin = begin
            self.flexible = False

            self.priority = 4

            if end is not None:
                if not isinstance(end, datetime):
                    end = datetime.strptime(end, '%m/%d/%y %H:%M:%S')
                self.end = end
                delta = self.end - self.begin
                self.hours = delta.days * 24 + round(2 * delta.seconds / 3600) / 2
            else:
                self.end = begin + timedelta(hours=hours)

        if self.flexible:
            assert priority in range(5), "priority value exceeds the range"
            self.priority = priority
            self.hours = hours

    def __str__(self):
        return f"Name: {self.name}\nFlexible: {self.flexible}\n" \
            f"Begin: {self.begin}\nEnd: {self.end}\nHours: {self.hours} hours\n" \
            f"Priority: {self.priority}"


class TaskBuilder:
    """
    This class handles the creation of Task objects.
    """

    def __init__(self):
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
        if self.name and self.hours:
            ret = Task(self.name, self.begin, self.end, self.priority, self.hours)
            self.reset()  # resets the current configuration
            return ret
        else:
            print('Either name or hours not filled in.')

    def reset(self):
        """Resets the attributes for building the next Task"""
        self.__init__()


if __name__ == '__main__':
    builder = TaskBuilder()
    # builder.get_data_from_input()
    # task = builder.build()
    # print(task)
    builder.set_priority(0).set_hours(3.5).set_name('testTask')
    task2 = builder.build()
    print(task2)
