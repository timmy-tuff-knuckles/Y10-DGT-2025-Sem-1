#assesment 2
#judah thornton
#28 may 2025
#v1

#ask for the length of fence and repate until a number above zero is entered

loop = '' #create a loop
while loop == '':
    question_legth = int(input('what it the length of the desired area to be measured in M: '))

    if question_legth>0: #do an if to make sure the number is over 0
        print (f'the length of the desired area is {question_legth}')
        question_width = int(input('what it the width of the desired area to be measured in M: '))

        if question_width>0:#ask for width than do a if
            print (f'the cost per meter of the desired area is {question_width}')
            cost_per_meter = int(input('what is the cost per meter in nzd: $'))

            if cost_per_meter>0:
                print (f'the cost per meter of the desired area is ${cost_per_meter}\n')
                awnser_fence_length = (question_width+question_legth) #put in then print the awnser 
                print (f'this is the length for fence you will need {awnser_fence_length}\n')
                awnser_cost=(awnser_fence_length*cost_per_meter)#this will caulculate the cost then print your cost awnser 
                print (f'this is how much it will cost for all the fencing ${awnser_cost}\n')
                continue_question = (input('if you would like to continue press enter if not, enter "no" bellow:\n')) #ask if they would like to finish or continue

                if continue_question == 'no' or "No": #if they awnser no then end the loop
                    loop = 'done :D'
                    
            else:#this will get a number above zero 
                print (f'the legth of the desired area is {cost_per_meter}')
                print ('please enter a valid number above zero')  

        else:#this will get a number above zero
            print (f'the width of the desired area is {question_width}')
            print ('please enter a valid number above zero')    
    
    else:#this will get a number above zero
        print (f'the length of the desired area is {question_legth}')
        print ('please enter a valid number above zero')