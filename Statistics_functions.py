import math

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def isSum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def average(grades):
    ''' note: mean and average are the same thing'''
    average = isSum(grades) / len(grades)
    return average

def variance(grades, average):
    '''subtract each grade from the average, then square it, then append
    it to a new list, take sum of that list as variance and divide it by
    the number of grades'''
    
    var_list = []
    
    for grade in grades:
        var_grade = (average - grade) ** 2
        var_list.append(var_grade)
        
    variance = isSum(var_list) / len(grades)
    
    return variance
    
def standard_deviation(variance):
    '''the standard deviation is the square root of the
    variance.'''
    
    std_dev = math.sqrt(variance)
    
    return std_dev

def Z_score(observation, mean, std_dev):
    '''Z score is the mean subtracted from an
    observation of the data(a list index here)
    divided by the standard deviation. This finds
    the standard deviations of observation above
    or below the mean. You then can look this up
    on a z table to find % samples above/below
    this thresh hold.

    What this means:
             ##################### 
             #Standard Deviations#
             #####################
    [-3]--[-2]--[-1]--[0]--[1]--[2]--[3]
     ^     ^     ^----68%----^   ^    ^
     ^     ^----------95%--------^    ^
     ^-----^----------99.7%------^----^
     #####Percent of observations######

     So what number is return can show what
     range the sample is. Discard scores beyond +3
     or -3 S.D.'''
    # pass functions to this

    z = (observation - mean) / std_dev

    return z


# Test lines
# Think about getting a z table somewhere online to plug in here....
print print_grades(grades)

print isSum(grades)

print average(grades)

print variance(grades, average(grades))

print standard_deviation(variance(grades, average(grades)))

for i in range(len(grades)):
    print Z_score(grades[i], average(grades), standard_deviation(variance(grades, average(grades))))
