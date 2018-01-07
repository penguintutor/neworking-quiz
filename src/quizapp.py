# This uses the dev branch of guizero which needs to be linked to the appropriate
# directory - in future this will use the normal production version of guizero 
from guizero.build.lib.guizero import App, Text, PushButton, info, MenuBar, Picture

import quizdetails
import time

class QuizApp():
    
    
    def __init__ (self, app):
        self.app = app
        self.quiz = quizdetails.QuizDetails() 

    def home(self):
        pass
    
    def upd_buttons(self):
        # Wait to give time for button to be released first
        time.sleep(1)
        if self.quiz.isFirst():
            self.left_button.text="Return"
            self.left_button.change_command(self.home)
        else:
            self.left_button.text="<< Previous"
            self.left_button.change_command(self.prev_question)
        if self.quiz.isLast():
            self.right_button.text="End Quiz"
            self.right_button.change_command(self.end_quiz)
        else:
            self.right_button.text="Next >>"
            self.right_button.change_command(self.next_question)
    
    # Load quiz from disk
    def load_quiz(self):
        self.quiz.load("quiz1.json")
        pass
    
    
    # Start the quiz
    def start_quiz(self):
        print ("Start Quiz")
        self.load_quiz()
        self.text_title.value = self.quiz.getTitle()
        #self.text_question_title.value = self.quiz.getQuestion().getTitle()
        self.upd_question()
        self.upd_buttons()
        
    # Update display of question
    def upd_question(self):
        print ("On question "+str(self.quiz.getQuestionNum()))
        this_question = self.quiz.getQuestion()
        self.text_question_title.value = this_question.getTitle()
        
        details = this_question.getDetails()
        self.text_question_details_1.value = details[0]
        self.text_question_details_2.value = details[1]
        self.text_question_details_3.value = details[2]
        self.text_question_details_4.value = details[3]
        self.text_question_details_5.value = details[4]
        
        options = this_question.getOptions()
        self.text_question_option_1.value = options[0]
        self.text_question_option_2.value = options[1]
        self.text_question_option_3.value = options[2]
        self.text_question_option_4.value = options[3]
        
        self.image_question.value = "images/"+this_question.getImage()
    
    # Move to prev question
    def prev_question(self):
        self.quiz.prevQuestion()
        self.upd_question()
        self.upd_buttons()
    
    
    # Move to next question
    def next_question(self):
        print ("Next Question")
        self.quiz.nextQuestion()
        self.upd_question()
        self.upd_buttons()
        
    # dummy command (see explanation later regarding guizero bug)
    def button_pressed(self):
        #print ("Button pressed")
        pass
        
    # End quiz
    def end_quiz(self):
        ##Todo implement this
        print ("Quiz ended")
    
    # Open a new quiz
    def file_open(self):
        ##Todo load different quiz
        pass
    
    # exit the self.app
    def file_exit(self):
        self.app.destroy()
    
    # About
    def help_about(self):
        info("About Quiz", "Created by Stewart Watkiss\nhttp://www.penguintutor.com")
    
    
    def setup_gui(self):    
        menubar = MenuBar(self.app,
                toplevel=["File", "Help"],
                options=[
                        [ ["Open",self.file_open],["Exit", self.file_exit] ] ,
                        [ ["About", self.help_about] ]
                        ])
        
        # column 0 and row 0 are used for dummy images for spacing
        # cols 1 to 5 used for actual display
        # dimensions shown to the right are minimum (using image)
        padding0_0 = Picture(self.app, image="layout/0_0.gif", grid=[0,0])       # 1 pixel
        padding1_0 = Picture(self.app, image="layout/1_0.gif", grid=[1,0])       # 100 pixel
        padding2_0 = Picture(self.app, image="layout/2_0.gif", grid=[2,0])       # 550 pixel
        padding2_0 = Picture(self.app, image="layout/3_0.gif", grid=[3,0])       # 100 pixel
        padding3_0 = Picture(self.app, image="layout/4_0.gif", grid=[4,0])       # 100 pixel
        
        padding0_2 = Picture(self.app, image="layout/0_2.gif", grid=[0,2])       # 100 pixel
        padding0_12 = Picture(self.app, image="layout/0_12.gif", grid=[0,12])    # 100 pixel
        
        self.text_title = Text(self.app, text="Quiz", size=30, grid=[2,1,2,1])
        image_logo = Picture(self.app, image="images/logo.gif", grid=[4,1,2,1])
        
        self.text_question_title = Text(self.app, text="Start Quiz", align="left", size=25, grid=[1,2,2,1])
        
        self.text_question_details_1 = Text(self.app, text="Enter the quiz by cabling up the patch-panel", align="left", size=18, grid=[1,3,3,1])
        self.text_question_details_2 = Text(self.app, text="the question number is shown at the top", align="left", size=18, grid=[1,4,2,1])
        self.text_question_details_3 = Text(self.app, text="the answer corresponds to a port on the", align="left", size=18, grid=[1,5,2,1])
        self.text_question_details_4 = Text(self.app, text="second row", align="left", size=18, grid=[1,6,2,1])
        self.text_question_details_5 = Text(self.app, text="", align="left", size=18, grid=[1,7,2,1])
        
        self.text_question_option_1 = Text(self.app, text="Press start when ready", align="left", size=18, grid=[1,8,2,1])
        self.text_question_option_2 = Text(self.app, text="", align="left", size=18, grid=[1,9,2,1])
        self.text_question_option_3 = Text(self.app, text="", align="left", size=18, grid=[1,10,2,1])
        self.text_question_option_4 = Text(self.app, text="", align="left", size=18, grid=[1,11,2,1])
        
        self.image_question = Picture(self.app, image="images/network1.gif", grid=[3,3,3,9])
        
        
        # Due to a bug in guizero (issue 103) the original button command is
        # set to a dummy method and change_command used to set the command instead
        self.left_button = PushButton(self.app, text="Return", command=self.button_pressed, grid=[1,13])
        self.left_button.change_command(self.prev_question)
        #self.left_button.hide()
        #self.right_button = PushButton(self.app, text="Start quiz", command=self.start_quiz, grid=[5,13])
        self.right_button = PushButton(self.app, self.button_pressed, text="Start quiz", grid=[5,13])
        self.right_button.change_command(self.start_quiz)
        self.app.display()