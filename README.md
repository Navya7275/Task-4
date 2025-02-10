# 🏋️ Workout Tracker

This is a Python-based workout tracking application that allows users to log their workouts, receive improvement suggestions, and visualize progress over time.

## 🚀 Features
- 📅 Log workout details (date, exercise, reps, weight)
- 📊 Generate workout progress reports with Matplotlib
- 🔍 Get personalized suggestions for improvement based on past workouts

## 📦 Installation

Ensure you have Python installed (recommended version: 3.8 or higher). Then, install the required dependencies:
```bash
pip install matplotlib
```

## 🛠️ Usage

### 🔹 Initializing the Tracker
```python
tracker = WorkoutTracker()
```

### 🔹 Logging Workouts
```python
import datetime
tracker.log_workout(datetime.date(2025, 2, 1), 'Bench Press', 10, 50)
tracker.log_workout(datetime.date(2025, 2, 5), 'Bench Press', 8, 55)
```

### 🔹 Getting Improvement Suggestions
```python
print(tracker.suggest_improvement('Bench Press'))
```

### 🔹 Generating a Report
```python
tracker.generate_report()
```
This will visualize your progress over time with a line graph.

## 📁 Project Structure
```
workout_tracker/
│-- tracker.py  # Contains the WorkoutTracker class
│-- README.md   # Project documentation
```

## 👥 Contributors
- **Navya Singhal**


