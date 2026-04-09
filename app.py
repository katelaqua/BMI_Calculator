def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI using weight in kg and height in meters.
    BMI = weight (kg) / (height (m) * height (m))
    """
    if height_m <= 0 or weight_kg <= 0:
        return "Error: Weight and height must be positive values"
    
    bmi = weight_kg / (height_m * height_m)
    return bmi

def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Main program
if __name__ == "__main__":
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        if isinstance(bmi, str):  # Error message
            print(bmi)
        else:
            classification = classify_bmi(bmi)
            print(f"\nYour BMI: {bmi:.2f}")
            print(f"Classification: {classification}")
    except ValueError:
        print("Error: Please enter valid numbers")
