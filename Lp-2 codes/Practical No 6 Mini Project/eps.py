def calculate_average(scores):
    return sum(scores) / len(scores)

def evaluate_performance(average_score):
    if average_score >= 90:
        return "Excellent"
    elif average_score >= 70:
        return "Good"
    elif average_score >= 50:
        return "Average"
    else:
        return "Poor"

def main():
    num_employees = int(input("Enter the number of employees: "))
    employee_data = {}

    for i in range(1, num_employees + 1):
        name = input(f"Enter the name of employee {i}: ")
        scores = []
        for j in range(1, 6):  # Assuming 5 criteria for evaluation
            score = float(input(f"Enter score for criteria {j} (out of 100) for {name}: "))
            scores.append(score)
        average_score = calculate_average(scores)
        performance = evaluate_performance(average_score)
        employee_data[name] = {"Average Score": average_score, "Performance": performance}

    # Display results
    print("\nEmployee Performance Evaluation Results:")
    print("=======================================")
    for name, data in employee_data.items():
        print(f"Employee: {name}")
        print(f"Average Score: {data['Average Score']}")
        print(f"Performance: {data['Performance']}")
        print()

if __name__ == "__main__":
    main()
