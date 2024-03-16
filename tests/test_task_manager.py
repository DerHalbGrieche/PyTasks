from src.task_manager import TaskManager

def test_add_task():
    task_manager = TaskManager()
    task_manager.add_task('task1')
    assert 'task1' in task_manager.list_tasks()
    task_manager.remove_task('task1')

def test_remove_task():
    task_manager = TaskManager()
    task_manager.add_task('task1')
    task_manager.remove_task('task1')
    assert 'task1' not in task_manager.list_tasks()

def test_complete_task():
    task_manager = TaskManager()
    task_manager.add_task('task1')
    task_manager.complete_task('task1')
    assert 'task1' in task_manager.list_completed_tasks()
    task_manager.remove_task('task1')

def test_list_tasks():
    task_manager = TaskManager()
    task_manager.add_task('task1')
    task_manager.add_task('task2')
    assert 'task1' in task_manager.list_tasks()
    assert 'task2' in task_manager.list_tasks()
    task_manager.remove_task('task1')
    task_manager.remove_task('task2')

def test_list_completed_tasks():
    task_manager = TaskManager()
    task_manager.add_task('task1')
    task_manager.add_task('task2')
    task_manager.complete_task('task1')
    assert 'task1' in task_manager.list_completed_tasks()
    assert 'task2' not in task_manager.list_completed_tasks()
    task_manager.remove_task('task1')
    task_manager.remove_task('task2')

def test_list_incomplete_tasks():
    task_manager = TaskManager()
    task_manager.add_task('task1')
    task_manager.add_task('task2')
    task_manager.complete_task('task1')
    assert 'task1' not in task_manager.list_incomplete_tasks()
    assert 'task2' in task_manager.list_incomplete_tasks()
    task_manager.remove_task('task1')
    task_manager.remove_task('task2')

def test_load_tasks():
    task_manager = TaskManager()
    task_manager.add_task('task1')
    task_manager.add_task('task2')
    task_manager = TaskManager()
    assert 'task1' in task_manager.list_tasks()
    assert 'task2' in task_manager.list_tasks()
    task_manager.remove_task('task1')
    task_manager.remove_task('task2')