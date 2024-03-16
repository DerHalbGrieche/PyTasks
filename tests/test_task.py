from src.task import Task

def test_create_task():
    task = Task('task1')
    assert task.name == 'task1'
    assert task.completed == False

def test_create_completed_task():
    task = Task('task1', True)
    assert task.name == 'task1'
    assert task.completed == True

def test_create_uncompleted_task():
    task = Task('task1', False)
    assert task.name == 'task1'
    assert task.completed == False

