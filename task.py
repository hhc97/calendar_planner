from datetime import datetime, timedelta


class Task:
    ''' 
    Args:
        name(str): the name of the task
        begin(datetime, or str): the begin time of the task. If it is str, it is in "09/19/18 13:55:26" format.
                    If begin is even, the task's flexibility is set to False, priority set to 4.
        end(datetiem, or str): the end time of the task. Same format as begin.
        priority (int): a value in [0, 1, 2, 3, 4].
        hours (float): will be rounded to the nearest 0.5
    '''
    
    def __init__(self, name, begin=None, end=None, priority=0, hours=1.0):
        self.flexible = True
        self.name = name
        self.begin = None
        self.end = None
        self.hours = round(2 * hours)/2
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
                self.hours = delta.days * 24 + round(2 * delta.seconds / 3600)/2
            else:
                self.end = begin + timedelta(hours=hours)

        if self.flexible:
            assert priority in range(5), "priority value exceeds the range"
            self.priority = priority
            self.hours = hours

    def __str__(self):
        return f"name: {self.name}\nflexible: {self.flexible}\n" \
            f"begin: {self.begin}\nend: {self.end}\nhours: {self.hours} hours\n" \
            f"priority: {self.priority}"


if __name__ == '__main__':
    task1 = Task("Be sexy", begin=datetime.now())
    print(task1)
    task2 = Task("Be bold")
    print(task2)
    task3 = Task("Be smart", begin="09/19/18 13:55:26", end=datetime.now())
    print(task3)
