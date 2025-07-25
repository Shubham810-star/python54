def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    """Return the BMI category based on WHO guidelines."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("====== BMI CALCULATOR ======")
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
        
        if weight <= 0 or height <= 0:
            print("Height and weight must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print("\n====== RESULT ======")
        print(f"Your BMI is: {bmi}")
        print(f"Health Category: {category}")

        if category == "Underweight":
            print("You might need to gain some weight. Consider consulting a doctor.")
        elif category == "Normal weight":
            print("Great! Keep maintaining your healthy lifestyle.")
        elif category == "Overweight":
            print("Try to engage in more physical activity and watch your diet.")
        else:
            print("Health alert: It is advisable to consult with a healthcare professional.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
