"""This section receives input from the users which will be used during calculation and file creation"""
fullname = input('what is your fullname?')

"""Float is used because weight can have decimal point"""
height = float(input('what is what your height in m'))
weight = float(input('what is what your weight in kg'))

"""The formular for bmi is weight/height squared"""
bmi = weight/(height**2)

"""Here, I created a variable to save the fullname and replace every space between with an underscore and add a txt extension since this will be our file name"""
filename = fullname.replace(' ','_')
filename_ext = filename + '.txt'

print(f' Your BMI is:{bmi}')

"""My Function with conditional statements conveying comments for every weight range"""
def calc_bmi():
    if bmi < 18.5:
        print(f'{fullname}, you are underweight')
    elif bmi < 25:
        print(f'{fullname}, you are within the normal weight')
    elif  bmi < 30:
        print(f'{fullname}, you are overweight')
    elif  bmi < 35:
        print(f' {fullname}, you are obese')
    else:
        print(f'{fullname}, you are clinically obese')


calc_bmi()
"""Opening of a file with each input received and all the details"""
with open(filename_ext, 'a') as new_file:
    new_file.write(f'\n Fullname: {fullname}, \n Height: {height} ft, \n Weight: {weight} kg \n BMI: {bmi} \n \n')
