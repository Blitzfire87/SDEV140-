#Program: Tricky_Trivia_Final_Project.py
#Author: Darren DeLaurentis
#Class: SDEV140
#Purpose: Final Project! Create a Trivia Game that allows user to pick from multi-choice questions
#                        User is scored based on correct/incorrect answers






import tkinter as tk


class Trivia:

    

    #Function that acts as a constructor
    #Holds all values necessary to run program
    
    def __init__(self):


        self.qno = 1

        self.disp_title()

        self.disp_ques(self.qno)

        self.opt_sel = tk.IntVar()

        self.disp_opt(self.qno)

        self.buttons()

        self.total_size = len(questions)

        self.correct = 0


        

    #Function used to display the trivia results in the second window
        
    def disp_res(self):

        #Positioning the score labels in the results window

        wrong_count = self.total_size - self.correct

        correct = f"Correct: {self.correct}"

        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.total_size * 100)

        result = f"Score: {score}%"
              

        ws2 = tk.Tk() #Window 2 and its respective geometry

        ws2.geometry("800x650")

        ws2.title("Tricky Trivia Results!")        

        window = tk.Toplevel(ws2)

        summary = tk.Label(ws2, text = f"{result}\n{correct}\n{wrong}", width = 60,fg = "blue", font = ("ariel", 12, "bold"),

                    anchor = "w", wraplength = 700, justify = "center")

        summary.place(x = 1, y = 1)

        y_val = 80                

        


        #Positioning for the incorrectly answered questions/correct answers to be displayed

        for each in incorrect_questions:

            question = tk.Label(ws2, text = questions[each][0], width = 60, font = ("ariel", 12, "bold"),

                        anchor = "w", wraplength = 700, justify = "center")

            question.place(x = 1, y = y_val)

            correct = questions[each][2] - 1

            answer = tk.Label(ws2, text = questions[each][1][correct], width = 60,fg = "green", font = ("ariel", 10, "bold"),

                        anchor = "w", wraplength = 700, justify = "center")

            answer.place(x = 1, y = y_val + 30)

            y_val += 70
    



        #Function used to return the correct answers

    def check_ans(self, qno):

        #Compare answer selected to the correct answer from questions dictionary

        if self.opt_sel.get() == questions[qno][2]:

            return True
        
        else:

            incorrect_questions.append(qno)

            


    def next_btn(self):

        
        #If chosen answer is correct, increase correct count by 1 


        if self.check_ans(self.qno):

            self.correct += 1



        #Increase by one to move to next question in dictionary

        self.qno +=1


        #Check if there are no more questions in dictionary

        #Show results and then close window 



        if self.qno > self.total_size:

            self.disp_res()

            ws.destroy()           



        #Display next question and options

        else:

            self.disp_ques(self.qno)

            self.disp_opt(self.qno)         



    #Creation of the "next" and "quit" buttons with their respective geometry
    
    def buttons(self):

        next_button = tk.Button(ws, text = "Next", command = self.next_btn, width = 10,

                             bg = "black", fg = "white", font = ("ariel", 16, "bold"))



        next_button.place(x = 350, y = 380)


        quit_button = tk.Button(ws, text = "Quit", command = ws.destroy, width = 5,

                             bg = "black", fg = "white", font = ("ariel", 16, "bold"))



        quit_button.place(x = 700, y = 50)
        


    def disp_opt(self, qno):

        # destroy the previous question's radio buttons

        for question in questions_holder:


            question.destroy()


        loop_val = 0

        y_val = 150

        opt_val = 1

        self.opt_sel.set(0)

        # loop through and display all answers in the current question

        for option in questions[self.qno][1]:

            radio_btn = tk.Radiobutton(ws, text = questions[self.qno][1][loop_val], variable = self.opt_sel, value = opt_val, font = ("ariel", 14))

            radio_btn.place(x = 100, y = y_val)


            # increase variables for next pass through in loop

            loop_val += 1

            y_val += 40

            opt_val += 1


            # add radio buttons to list so they can be sought and destroyed next time this function is called

            questions_holder.append(radio_btn)


  
                      
    #Position of question labels
            
    def disp_ques(self, qno):

        question = tk.Label(ws, text = questions[self.qno][0], width = 60, font = ("ariel", 16, "bold"),

                    anchor = "w", wraplength = 700, justify = "center")


        question.place(x = 70, y = 100)



    #Position of the title label displayed at the top of the window throughout the game

    def disp_title(self):


        title = tk.Label(ws, text = "Tricky Trivia!", width = 50, bg = "purple", fg = "white",

                      font = ("ariel", 20, "bold"))


        title.place(x = -40, y = 2)


        #Image and text displayed on first window
        

        photo = tk.PhotoImage(file = 'BeatlesPoint.png')
        
        label = tk.Label(image = photo)
        
        label.image = photo

        label.place(x = 500, y = 200)

        

        subtext1 = tk.Label(ws, text = "Good Luck!", width = 23, fg = "blue",

                      font = ("times new roman", 14, "bold"))

        subtext1.place(x = 502, y = 352)
        

              
#Window creation

ws = tk.Tk()


ws.geometry("800x450")


ws.title("Tricky Trivia!")



#Dictionary for questions and answer options with the key set to the correct answer

questions = {


  1: ["Which country was not invaded by Germany during World War 2?",["Norway","Greece","Finland","France"],3],



  2: ["How many layers make up the Earth's Atmosphere?",["Five","Three","Four","Two"],1],



  3: ["Christian Bale stars as Batman in which movie?",["Batman Forever","The Batman","The Dark Knight","Batman and Robin"],3],



  4: ["How many players take the field in a baseball game?",["11","8","6","9"],4],



  5: ["Who was not a member of The Beatles?",["George Harrison","Paul McCartney","Ringo Starr","John Bonham"],4],



  6: ["What year was the Soviet Union dissolved?",["1989","1991","1994","1986"],2],



  7: ["The Jets are an NHL Hockey team from which city?",["New York","Jacksonville","Winnipeg","Anaheim"],3],



  8: ["When was the World Wide Web first launched for public use?",["1993","1990","1997","1994"],1] 

 

}


#List to hold question radio button widgets so they can be deleted before new questions are placed

questions_holder = []

incorrect_questions = []

trivia = Trivia()



ws.mainloop()         







