#Declaring Variables and Identifying Data Types
from pyscript import display, document


name = "John Christopher O. Carreon" #This String
young = 15 #This Integer
cm = 124 #This Integer
countries = ['Spain', 'Poland', 'USA'] #This a List
new_student = False #This is A Bool
mylikes = {'color':'emerald green',
           'Car_brand':'Ford',
           'Sizeofshoes':'14',
           'best friend':'None'} #This is A Dictionary
fruits = set(['Mango', 'Lcyhee', 'Apple', 'Bananas','Pineapple']) #This is a Set
weeks = (1,2,3,4,5,6,7) #This is a Tuple

display(f'Hello and welcome to my webpage I am <i>{name}</i> and I am {young} years old and my hight is {cm}cm', target = 'aboutME')
document.getElementById('aboutME').innerHTML = f'Hello and welcome to my webpage I am <i>{name}</i> and I am {young} years old and my hight is {cm}cm'

display(f'Here are some of the countries I would love to go to {countries}, as well as some of my likes {mylikes}', target = 'countries')

display(f'Some of the fruits that I eat are {fruits}, as well as the weeks {weeks}, and last it is {new_student} I am not new student', target = 'end')
