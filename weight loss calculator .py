print("=== Weight Loss Calculator ===")

current_weight = float(input("Current weight (kg): "))
target_weight = float(input("Target weight (kg): "))
height = float(input("Height (m): "))

weight_to_lose = current_weight - target_weight
bmi = current_weight / (height ** 2)

print(f"\nCurrent BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Healthy weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print(f"Weight difference: {weight_to_lose:.1f} kg")
