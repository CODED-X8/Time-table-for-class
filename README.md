# Class Timetable Script

This Python script helps manage and check class schedules by providing the next class, morning or afternoon classes, or all classes for the current or a specified date. The script uses the `pytz` library to display the schedule in Indian Standard Time (IST) and formats the output in a clean table using `tabulate`.

## Features

- Displays the current day and time based on IST.
- Retrieves the next class, morning classes (AM), afternoon classes (PM), or all classes for the current day.
- Supports checking class schedules for any date by entering the date in `DD MM YYYY` format.
- Excludes weekends and provides a message for no classes on Saturdays and Sundays.
- Calculates and displays both start and end times for each class, factoring in longer durations for labs.

## Commands

The following commands can be entered to interact with the timetable:

| Query           | Command           |
|-----------------|-------------------|
| Next class      | `Next`            |
| Morning classes | `AM`              |
| Afternoon classes | `PM`              |
| All classes     | `All`             |

By default, commands show today's classes. You can also specify a date to see the schedule for a different day by appending the date in the format `DD MM YYYY`, e.g., `AM 06 09 2024`.

## Prerequisites

Make sure you have the following Python libraries installed:
- `pytz`
- `tabulate`

Install them using `pip`:
```bash
pip install pytz tabulate
