bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi)) # Converts the float BMI to an integer by truncating the decimal part

print(round(bmi)) # Rounds the float BMI to the nearest integer

print(round(bmi, 2)) # Rounds the float BMI to 2 decimal places


print(f"Your BMI is {bmi:.2f}")  # Formatted string to display BMI with 2 decimal places