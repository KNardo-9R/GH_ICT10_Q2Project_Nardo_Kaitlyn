from pyscript import display, document 

# WANNA GET GWA USING SUBJECTS AND SUBJECT UNITS 

def getting_info(e): 

# -----establishing values and variables

    # output no repeat
    document.querySelector('#studentsubjects').innerText = " "
    document.querySelector('#popup').innerText = " "

    # list for SUBJECTS; combines strings
    subject_lists1 = ['Science', 'Math', 'Filipino']
    subject_lists2 = ['English', 'SS', 'PE']
    subject_list = subject_lists1 + subject_lists2 # combines strings for one list 

    # tuple for SUBJECT UNITS
    subject_units = (5,5,3,5,4,1)

    # variables for inputted SUBJECT VALUES in html
    Science = float(document.getElementById('ScienceG').value)
    Math = float(document.getElementById('MathG').value)
    Filipino = float(document.getElementById('FilG').value)
    English = float(document.getElementById('EngG').value)
    SS = float(document.getElementById('SSG').value)
    PE = float(document.getElementById('PEG').value)

    # list for all the subjects
    subject_values = [Science, Math, Filipino, English, SS, PE]

# ------ computation for GWA
    # multiplying each grade of each subject by its unit to get the product (individual subject value)

    Science_value = subject_values[0] * subject_units[0]
    Math_value = subject_values[1] * subject_units[1]
    Filipino_value = subject_values[2] * subject_units[2]
    English_value = subject_values[3] * subject_units[3]
    SS_value = subject_values[4] * subject_units[4]
    PE_value = subject_values[5] * subject_units[5]
 
    # adding up the products (individual subject values) 
    Sum = Science_value + Math_value + Filipino_value + English_value + SS_value + PE_value 

    # sum of units (from earlier tuple)
    Unit_sum = subject_units[0] + subject_units[1] + subject_units[2] + subject_units[3] + subject_units[4] + subject_units[5]

    # dividing sum of subject values (the products) by the sum of units (how many units there are)
    GWA =  Sum / Unit_sum

    Subjects = f'''

    {subject_list[0]}: {subject_values[0]:.2f}
    {subject_list[1]}: {subject_values[1]:.2f}
    {subject_list[2]}: {subject_values[2]:.2f}
    {subject_list[3]}: {subject_values[3]:.2f}
    {subject_list[4]}: {subject_values[4]:.2f}
    {subject_list[5]}: {subject_values[5]:.2f}

    '''

    display(Subjects, target='studentsubjects')
    display(f'Your General Weighted Average is {GWA:.2f}',target='popup')

    
