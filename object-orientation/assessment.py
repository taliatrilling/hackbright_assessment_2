"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

TALIA YOU STILL NEED TO DO THIS!
ALSO ADD DOCSTRINGS TO EACH CLASS AND SO ON
"""

class Student(object):
	def __init__(self, first_name, last_name, address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address	

class Question(object):
	def __init__(self, question, correct_answer):
		self.question = question
		self.correct_answer = correct_answer

	def ask_and_evaluate(self):
		guess = raw_input(self.question + " ")
		if guess == self.correct_answer:
			print True
		else:
			print False

class Exam(object):
	questions = []
	def __init__(self, name):
		self.name = name

	def add_question(self, question, correct_answer):
		question = Question(question, correct_answer)
		self.questions.append(question)

	def administer(self):
		score = 0
		for question in self.questions:
			Question.ask_and_evaluate(question)
			#this seems weird to me-- I wanted to just do "if Question.ask_and_evaluate:" "score +=1" but that refused to work for me
			if True: 
				score += 1
		return score

def take_test(exam, student):
	pass



