# Python SOLID Principles and TDD Project

This project is a simple task manager application developed in Python, applying SOLID principles and Test-Driven Development (TDD).

## SOLID Principles

SOLID is an acronym for the first five object-oriented design principles:

- S: Single Responsibility Principle (SRP)
- O: Open-Closed Principle (OCP)
- L: Liskov Substitution Principle (LSP)
- I: Interface Segregation Principle (ISP)
- D: Dependency Inversion Principle (DIP)

I have tried to integrate them in this Project

## Test-Driven Development (TDD)

TDD is used to automatically test your code, allowing to spot a problem faster. I have written Tests for the 2 Classes, which assure that each function works as intended.

## Project Structure

The project is divided into two main parts:

- `src/`: This directory contains the application code. It includes the `TaskManager` class in [`task_manager.py`](src/task_manager.py) and the `Task` class in [`task.py`](src/task.py).
- `tests/`: This directory contains the unit tests for the application. It includes tests for the `TaskManager` class in [`test_task_manager.py`](tests/test_task_manager.py) and the `Task` class in [`test_task.py`](tests/test_task.py).

## Running the Application

To run the application, clone the repository, activate the venv, and run the following command:

```sh
./tasks [COMMAND] [TASK]
```
