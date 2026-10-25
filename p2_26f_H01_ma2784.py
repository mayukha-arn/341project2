#send all output to the output.txt file
output_file="output.txt"
log784=[] #lines shown on screen will be stored in this list

EPS784="ε" #epsilon variable to store read, popped, and pushed
accepted_states={11} #st
header784 = ("Project 2 for CS 341 \n" "Second Number: H01 \n" "Written by: Mayukha Ajeesh Ramsha Nath, ma2784\n" "Instructor: Marvin Nakayama, marvin@njit.edu")

print(header784)

#implementing PDA

#need to get output to output.txt file
#store lines in log (method name: log784)
#store empty string variable as epilon

#needed methods: 
# general: log, output, input, 
#digits (store numerical alphabet), operator (store operator alphabet), 
# transitions show the logic of each state transition
#process method to read and output
#read to read user input
#function to analyze strings
#main method to run the program

#print to screen and remember output lines for output
def output784(text):
    log784.append(text)
    print(text)

#log prompt and answer
def input784(prompt):
    text=input(prompt)
    log784.append(prompt+text)
    return text

#digits method
def digits784(ch):
    return ch in "0123456789"
#operators method
def operators784(ch):
    return ch in "+-*/"

def transition(state,ch,stack):
    top=stack[-1] if stack else EPS784
    #beginning: y c p^k c
    if state==1: #start state q1
        f
    if state==1:
        f
    if state==3:
        f
    #expression E - operations and arithmetic
    if state==4:
        f
    if state==5: #digits before any dot
        f
    if state==6: #leading dot without any digits
        f
    if state==7: #digits after the dot
        f
    if state==8: #just closed )
        f
    if state==9: #first y of pair pops A or first r pops $
        f
    if state==10: #second y of pair pops A or pair pops nothing
        f
    #accept state has no edges so anything greater will crash
    return None

def process784(string):
    state=1
    stack=[]
    output784(f"Processing string: {string}")

def read784():
    prompt="fill in."

def pdaanalyzer784():
    m=read784()
    output784(f"value of m: {m}")

def main784():
    pdaanalyzer784()
    with open(output_file,"w") as f:
        for line in log784:
            f.write(line+"\n")

main784()
    