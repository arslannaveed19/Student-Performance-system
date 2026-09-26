# Student Performance Management System

A simple **Student Marks Management System** built with **Python and Pandas**.

This project stores student data in a Pandas DataFrame and provides different options to analyze student marks through a console-based menu.

## Features

The program provides the following features:

1. Display all student records
2. Calculate average marks
3. Find highest marks
4. Find lowest marks
5. Count passing students
6. Count failing students
7. Find the student with highest marks
8. Filter students based on minimum marks
9. Exit the program

## Technologies Used

- Python
- Pandas

## Student Data

Each student record contains:

- Student Name
- Roll Number
- Marks

Example data:

| Student Name | Roll Number | Marks |
|--------------|-------------|-------|
| Ali          | 101         | 85    |
| Ahmed        | 102         | 72    |
| Sara         | 103         | 45    |
| Usman        | 104         | 91    |
| Ayesha       | 105         | 58    |

## Pandas Functions Used

This project uses several useful Pandas operations:

- `pd.DataFrame()` – Creates a DataFrame
- `.mean()` – Calculates average marks
- `.max()` – Finds maximum marks
- `.min()` – Finds minimum marks
- `.sum()` – Counts passing/failing students
- `.loc[]` – Selects student records
- `.idxmax()` – Finds the index of the student with highest marks
- Boolean filtering – Filters students based on marks

## Passing Criteria

A student is considered **Passing** if:

```text
Marks >= 50
