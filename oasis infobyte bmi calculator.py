print("Welcome to BMI Calulator!")
def get_valid_weight():
    while True:
        try:
            weight = float(input("Please enter your weight in kilograms: "))
            if 20 <= weight <= 300:
                return weight
            else:
                print("Invalid input. Weight must be between 20 and 300 kilograms.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_valid_height():
    while True:
        try:
            height = float(input("Please enter your height in meters: "))
            if 0.5 <= height <= 2.5:
                return height
            else:
                print("Invalid input. Height must be between 0.5 and 2.5 meters.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
weight = get_valid_weight()
height = get_valid_height()

bmi = weight /(height**2)
bmi=round(bmi,2)

print("According to the BMI categories defined by the World Health Organization (WHO):")
if bmi < 18.5:
    print(f"Your BMI value is {bmi} and you are Underweight")
elif bmi>=18.5 and bmi<24.9:
    print(f"Your BMI value is {bmi} and you are of normal weight")
elif bmi>=25 and bmi<29.9:
    print(f"Your BMI value is {bmi} and you are Overweight")
else:
    print(f"Your BMI value is {bmi} and you are obese")