from datetime import datetime, timedelta

class Task:
    def __init__(self, name, begin = None, end = None, priority = 0, hours = 1):
        self.flexible = True
        self.name = name
        self.begin = None
        self.end = None
        self.hours = hours
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
                self.hours = delta.days * 24 + delta.seconds/3600
            else:
                self.end = begin + timedelta(hours=hours)

        if self.flexible:
            assert priority in range(5), "priority value exceeds the range"
            self.priority = priority
            self.hours = hours

    def __str__(self):
        return f"name: {self.name}\nflexible: {self.flexible}\nbegin: {self.begin}\nend: {self.end}\nhours: {self.hours} hours"

if __name__ == '__main__':
    task1 = Task("Be sexy", begin=datetime.now())
    print(task1)
    task2 = Task("Be bold")
    print(task2)
    task3 = Task("Be smart", begin="09/19/18 13:55:26", end=datetime.now())
    print(task3)
