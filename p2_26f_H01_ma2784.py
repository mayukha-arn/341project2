#send all output to the output.txt file
output_file="output.txt"
log784=[] #lines shown on screen will be stored in this list

EPS784="ε" #epsilon variable to store read, popped, and pushed
accepted_states={11} #st
header784 = ("Project 2 for CS 341 \n" "Section Number: H01 \n" "Written by: Mayukha Ajeesh Ramsha Nath, ma2784\n" "Instructor: Marvin Nakayama, marvin@njit.edu")

print(header784)
log784.append(header784)

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
        if ch=="y":
            return 2,EPS784,"$"
        return None
    if state==2:
        if ch=="c":
            return 3,EPS784,EPS784
        return None
    if state==3:
        if ch=="p":
            return 3,EPS784,"A"
        elif ch=="c":
            return 4,EPS784,EPS784
        return None
    #expression E - operations and arithmetic
    if state==4:
        if digits784(ch):
            return 5,EPS784,EPS784
        elif ch==".":
            return 6,EPS784,EPS784
        elif ch=="(":
            return 4,EPS784,"("
        return None
    if state==5: #digits before any dot
        if digits784(ch):
            return 5,EPS784,EPS784
        elif ch==".":
            return 7,EPS784,EPS784
        return None
    if state==6: #leading dot without any digits
        if digits784(ch):
            return 7,EPS784,EPS784
        return None
    if state==7 or state==8: #digits after the dot
        if state==7 and digits784(ch):
            return 7,EPS784,EPS784
        elif operators784(ch):
            return 4,EPS784,EPS784
        elif ch==")" and top=="(":
            return 8,"(",EPS784
        elif ch=="r" and top=="A":
            return 9,"A","A"
        elif ch=="r" and top=="$":
            return 9,"$","$"
        return None
    #end of expression y^(2k) r
    if state==9: #first y of pair pops A or first r pops $
        if ch=="y" and top=="A":
            return 10,"A",EPS784
        elif ch=="r" and top=="$":
            return 11,"$",EPS784
        return None
    #second y of pair pops nothing
    if state==10: #second y of pair pops A or pair pops nothing
        if ch=="y":
            return 9,EPS784,EPS784
        return None
    #accept state has no edges so anything greater will crash
    return None

def process784(string):
    state=1
    stack=[]
    output784(f"Start date: q{state}")
    for idx,ch in enumerate(string):
        output784(f"Read: {ch}")
        result=transition(state,ch,stack)
        if result is None:
            output784(f"PDA crashed at index {idx} with input {ch}. Current stack: {stack}")
            return False
        state,new_top,push= result
        output784(f"Transition to state q{state}, pop: {new_top}, push: {push}")
        if new_top != EPS784 and stack:
            stack.pop()
        if push != EPS784:
            stack.append(push)
        output784(f"Current stack: {stack}")
        state=next_state
        return state in accepted_states
        
def read784():
    prompt="Enter an integer explaining the number of input strings to be analyzed: "
    while True:
        text=input784(prompt)
        try:
            m=int(text)
            if m>0:
                return m
        except ValueError:
            output784("Invalid input. Please enter a positive integer.")

def pdaanalyzer784():
    m=read784()
    output784(f"value of m: {m}")
    if m==0:
        output784("No strings to analyze. Exiting.")
        return
    for i in range(1,m+1):
        string=input784(f"Enter string {i}: ")
        output784(f"Analyzing string {i}: {string}")
        output784(f"Result: {'Accepted' if process784(string) else 'Rejected'}")
        accepted=process784(string)
        if accepted:
            output784(f"String {i} is accepted by the PDA.")
        else:
            output784(f"String {i} is rejected by the PDA.")
        output784(f"End of analysis for string {i}.\n")

def main784():
        pdaanalyzer784()
        with open(output_file,"w") as f:
            for line in log784:
                f.write(line+"\n")

main784()
    