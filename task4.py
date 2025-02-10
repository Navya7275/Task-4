import matplotlib.pyplot as plt
import datetime

class WorkoutTracker:
    def __init__(self):
        self.workouts = []
    
    def log_workout(self, date, exercise, reps, weight):
        self.workouts.append({
            'date': date,
            'exercise': exercise,
            'reps': reps,
            'weight': weight
        })
    
    def suggest_improvement(self, exercise):
        exercise_data = [w for w in self.workouts if w['exercise'] == exercise]
        if not exercise_data:
            return "No data available for this exercise."
        
        latest = max(exercise_data, key=lambda x: x['date'])
        avg_reps = sum(w['reps'] for w in exercise_data) / len(exercise_data)
        avg_weight = sum(w['weight'] for w in exercise_data) / len(exercise_data)
        
        suggestion = "Consider increasing "
        if latest['reps'] < avg_reps:
            suggestion += "your reps. "
        if latest['weight'] < avg_weight:
            suggestion += "your weight. "
        
        return suggestion if suggestion != "Consider increasing " else "Keep up the good work!"
    
    def generate_report(self):
        exercises = list(set(w['exercise'] for w in self.workouts))
        
        for exercise in exercises:
            dates = [w['date'] for w in self.workouts if w['exercise'] == exercise]
            weights = [w['weight'] for w in self.workouts if w['exercise'] == exercise]
            
            plt.plot(dates, weights, marker='o', label=exercise)
        
        plt.xlabel("Date")
        plt.ylabel("Weight (kg)")
        plt.title("Workout Progress Over Time")
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()

# Example usage
tracker = WorkoutTracker()
tracker.log_workout(datetime.date(2025, 2, 1), 'Bench Press', 10, 50)
tracker.log_workout(datetime.date(2025, 2, 5), 'Bench Press', 8, 55)
tracker.log_workout(datetime.date(2025, 2, 10), 'Bench Press', 12, 60)
tracker.log_workout(datetime.date(2025, 2, 2), 'Squat', 10, 80)
tracker.log_workout(datetime.date(2025, 2, 6), 'Squat', 12, 85)
tracker.log_workout(datetime.date(2025, 2, 11), 'Deadlift', 8, 100)
tracker.log_workout(datetime.date(2025, 2, 15), 'Deadlift', 10, 105)


print(tracker.suggest_improvement('Bench Press'))
tracker.generate_report()
