
# this program calculated the percentage # of male and female student in the class
 

# this ask for number of male sudent registured in the class
numberOfMale = int(input("enter the number of male and female student  registared ".title() ))

# this asked for the number of fenale sudent registurd in the class
numberOfFemale = int(input("enter the number of female sudent registuredc ".title() ))

# percentage of male student 
percentageOfMaleStudent = (numberOfMale / 20) * 100

# percentage of female sudent
percentageOfFemaleStudent = (numberOfFemale / 20) * 100


print(f"\n\nthe percentage of male sudent in the class is % \
      {percentageOfMaleStudent:.2f}\nthe perecntage of female Student is % \
      {percentageOfFemaleStudent:.2f}".title())
