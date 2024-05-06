class User:
    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role

    def authenticate(self, login_attempt, password_attempt):
        if self.login == login_attempt and self.password == password_attempt:
            return True
        else:
            return False

    def authorize(self, required_roles):
        if self.role in required_roles:
            return True
        else:
            return False


class Project:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def find_task_by_name(self, name):
        return [task for task in self.tasks if task.name == name]

    def find_task_by_start_date(self, start_date):
        return [task for task in self.tasks if task.start_date == start_date]

    def find_task_by_end_date(self, end_date):
        return [task for task in self.tasks if task.end_date == end_date]

    def is_completed(self):
        return all(task.status for task in self.tasks)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'tasks': [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data['name'], data['description'], data['start_date'], data['end_date'])
        for task_data in data['tasks']:
            task = Task.from_dict(task_data)
            project.add_task(task)
        return project


class Task:
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = False
        self.performers = []

    def change_status(self):
        self.status = not self.status

    def add_performer(self, performer):
        self.performers.append(performer)

    def remove_performer(self, performer):
        self.performers.remove(performer)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'status': self.status,
            'performers': self.performers
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data['name'], data['description'], data['start_date'], data['end_date'])
        task.status = data['status']
        task.performers = data['performers']
        return task


def test_user_authentication():
    user = User("test_user", "password123", "admin")
    assert user.authenticate("test_user", "password123") is True
    assert user.authenticate("test_user", "wrong_password") is False


def test_user_authorization():
    user = User("test_user", "password123", "admin")
    assert user.authorize(["admin"]) is True
    assert user.authorize(["user"]) is False


def test_project_add_remove_task():
    project = Project("Test Project", "Description", "2022-01-01", "2022-01-10")
    task = Task("Task 1", "Task Description", "2022-01-02", "2022-01-05")
    project.add_task(task)
    assert len(project.tasks) == 1
    project.remove_task(task)
    assert len(project.tasks) == 0


def test_project_find_task_by():
    project = Project("Test Project", "Description", "2022-01-01", "2022-01-10")
    task = Task("Task 1", "Task Description", "2022-01-02", "2022-01-05")
    project.add_task(task)
    found_tasks = project.find_task_by_name("Task 1")
    assert len(found_tasks) == 1
    found_tasks = project.find_task_by_end_date("2022-01-05")
    assert len(found_tasks) == 1
    found_tasks = project.find_task_by_start_date("2022-01-02")
    assert len(found_tasks) == 1


def test_project_is_completed():
    project = Project("Test Project", "Description", "2022-01-01", "2022-01-10")
    task = Task("Task 1", "Task Description", "2022-01-02", "2022-01-05")
    project.add_task(task)
    assert project.is_completed() == False
    project.remove_task(task)
    task.change_status()
    project.add_task(task)
    assert project.is_completed() == True


def test_project_to_from_dict():
    project = Project("Test Project", "Description", "2022-01-01", "2022-01-10")
    task = Task("Task 1", "Task Description", "2022-01-02", "2022-01-05")
    project.add_task(task)
    assert project.to_dict() == project.from_dict(project.to_dict()).to_dict()


def test_task_change_status():
    task = Task("Task 1", "Task Description", "2022-01-02", "2022-01-05")
    assert task.status == False
    task.change_status()
    assert task.status == True


# def test_task_add_remove_performer():
#     task = Task("Task 1", "Task Description", "2022-01-02", "2022-01-05")
#     task.add_performer("Performer 1")
#     assert len(task.performers) == 1
#     task.remove_performer("Performer 1")
#     assert len(task.performers) == 0
