# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: w2053072
# Date: 2023/12/14


#part 1
from graphics import *

inputMarks = []  # creating an empty list called inputMarks
progress_count = 0 # used to count the number of progress students
trailer_count = 0 # used to count the number of trailer students
retriever_count = 0 # used to count the number of retriever students
exclude_count = 0 # used to count the number of excclude students
symbol = ''  # assigning an empty string


def get_credits(valid):
    '''prompts for inputs and validates if they are in the allowed rage'''
    while True:
        try:
            credits=int(input(valid))
            if credits not in range(0,121,20): # check if the entered inputs are in the valid rage
                        print('Out of range \n')
                        continue
            return credits  # return the input values in pass_credit, defer_credit and fail_credit
        except ValueError: # handle the error if integer value is not entered
            print('Integer required \n')

def draw_rectangle(startx, starty, endx, endy, colour):
    '''draw coloumns in graphics window with relative cordinates'''
    box = Rectangle(Point(startx, starty), Point(endx, endy))
    box.setFill(colour)
    box.draw(window) # draw the specific rectangle on the graphic window

def texts(start, end, text, size, style, colour):
    '''draw texts in the graphics window with specified attributes'''
    title = Text(Point(start, end), text)
    title.setSize(size)
    title.setStyle(style)
    title.setFill(colour)
    title.draw(window) # draw the texts in the graphic window

file = open('inputfile.txt', 'w') # create a text file named inputfile

print('Hello!') # welcome message for the user

while True:
    status = input('Are you a student or staff? ').lower() # asking the user if he/she is staff or student and changing the word into lowercase
    print() # print an empty line for better readability

    # check whether the user is a student or a staff member 
    if status == 'student':
        print('Logged as a stuent \n')
        break
    elif status == 'staff':
        print('Logged as staff \n')
        break
    else:
        print('You must enter student or staff') # handle the error if anything else was entered
        
   
# loop to gather student credits and determine their grade until the user decides to quit.
while symbol != 'q':
    pass_credit = get_credits('Please enter your credits at pass: ') # get the crdits at fail
    defer_credit = get_credits('Please enter your credits at defer: ') # get the crdits at fail
    fail_credit = get_credits('Please enter your credits at fail: ') # get the crdits at fail
                 
    if pass_credit+defer_credit+fail_credit!=120: # check if the total credits entered by the user are coorect
        print('Total incorrect \n')
        continue
    else:
        if pass_credit==120: # for progress students
            grade='progress'
            progress_count += 1 # increment the prgress count 
        elif pass_credit==100: # for module trailer students
            grade='Progress (module trailer)'
            trailer_count += 1 # increment the trailer count
        elif fail_credit>=80: # for exclude students
            grade='Exclude' # increment the exclude count
            exclude_count += 1
        else: # for module retriever students
            grade='Do not Progress - module retriever' 
            retriever_count += 1 # increment the retriever count 


    print(grade) # display the determined grade to the user
    
    if status == 'student': # if a user is a student this will exit the program
            raise SystemExit
            
    inputMarks.append([pass_credit,defer_credit,fail_credit,grade]) # append the input data to the inputMarks list

    file.write(f"{grade} - {pass_credit}, {defer_credit}, {fail_credit}\n") # write the input data to inputfile.txt file

    #prompt the user if they want to enter another set of data
    print()
    print('Would you life to enter another data?')
        

    while True: 
        symbol=input("Enter 'y' for yes  or 'q' to quit and view results: ").lower() # prompt the user to enter 'y' to continue or 'q' to quit and view results 
        if symbol == 'y' or symbol == 'q':
            print()
            break 

        

window = GraphWin("Histogram", 600, 550) # creating the graphic window and naming it 'Histogram'
window.setBackground("white") # setting the backgrpund colour white

texts(180, 30, 'Histogram Results', 18, 'bold', 'black') # calling the text function for the title in graphic window

horizontal_line = Line(Point(50,450), Point(550,450)) # drawing a line in graphic window
horizontal_line.draw(window) # draw the line in graphic window

max_height = 350 # giving a max height for coloumns in graphic window
max_count = max(progress_count, trailer_count, retriever_count, exclude_count) # get the highest count in four grades
total_count = progress_count + trailer_count + retriever_count + exclude_count # get the total count in four grades

h1 = (max_height/max_count) * progress_count # get the coloumn 1 height with a logic
h2 = (max_height/max_count) * trailer_count # get the coloumn 2 height with a logic
h3 = (max_height/max_count) * retriever_count # get the coloumn 3 height with a logic
h4 = (max_height/max_count) * exclude_count # get the coloumn 4 height with a logic

texts(120, 440-h1, progress_count, 12, 'bold', '#848c97') # show the count in top of coloumn 1
texts(240, 440-h2, trailer_count, 12, 'bold', '#848c97') # show the count in top of coloumn 2
texts(360, 440-h3, retriever_count, 12, 'bold', '#848c97') # show the count in top of coloumn 3
texts(480, 440-h4, exclude_count, 12, 'bold', '#848c97') # show the count in top of coloumn 4

draw_rectangle(80, 450, 160, 450-h1, '#AEF8A1') # drawing coloumn 1 
draw_rectangle(200, 450, 280, 450-h2, '#A0C689') # drawing coloumn 2    
draw_rectangle(320, 450, 400, 450-h3, '#A7BC77') # drawing coloumn 3
draw_rectangle(440, 450, 520, 450-h4, '#D2B6B5') # drawing coloumn 4

texts(120, 460, 'Progress', 12, 'bold', '#848c97') # draw the bottom text of coloumn 1 
texts(240, 460, 'Retriever', 12, 'bold', '#848c97') # draw the bottom text of coloumn 2 
texts(360, 460, 'Trailer', 12, 'bold', '#848c97') # draw the bottom text of coloumn 3 
texts(480, 460, 'Excluded', 12, 'bold', '#848c97') # draw the bottom text of coloumn 4 

texts(180, 490, f'{total_count} outcomes in total', 16, 'bold', '#848c97') # draw the total outcomes in the graphic window

try:
    window.getMouse()
    window.close() # close the graphic window by clicking on it
except GraphicsError: # handling the error if the user close graphic window instead of clicking
     pass



#Part 2 - display entered data 
print('Part 2:')
for entry in inputMarks: # iterate through the list 'inputMarks' to display the data
    print(f"{entry[3]} - {entry[0]}, {entry[1]}, {entry[2]}") # display each entry in the list 



#Part 3 - read and display data from the 'input.txt' file
print()
try:
    with open('inputfile.txt', 'r') as file: # iterate through each line in the file
        print("Part 3:")
        for line in file:
            print(line.strip()) # print each line (strip any leading or trailing white spaces.)
            
except FileNotFoundError: # handle the case if the file is not found
    print("No progression data found.")       


 

