"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages offered by object orientation are abstraction, encapsulation, and 
   polymorphism. Abstraction refers to the fact that object oriented programming allows for certain details
   to remain hidden when using code, and that a user doesn't need to specifically understand the mechanics
   behind a method to use it, allowing them to focus on the more essential parts of the code and making the
   code more accessible. Encapsulation refers to the way that object oriented programming allows for data 
   to exist adjacent to its functionality. Finally, polymorphism refers to the way in which object orientation
   allows for code to take in different types of components without needing to write conditional statements 
   to account for these differing types.

2. What is a class?
   
   A class is a data type in Python that allows for the grouping of complex data and related functions (called 
   methods). 

3. What is an instance attribute?

   An instance attribute is a type of attribute that is defined by a specific instance of a class. For example,
   after instantiating an instance of a class, one can set an instance attribute for that instance, which can 
   either override existing class attributes, or be an entirely new attribute that now exists for that instance.

4. What is a method?

   A method is similar to a function, but unlike a function is associated with/defined within a specific class, 
   always takes in self as the first parameter, and this parameter does not need to be explicitly stated when
   calling the method. The self parameter can represent any class attribute, meaning that the method can 
   refer to any class attributes with the format self.attribute_name. Additionally, methods can call each other,
   further increasing the usefulness of them.

5. What is an instance in object orientation?

   In object orientation, an instance, also known as an object, is a specific occurence of a class, rather
   than the whole class itself. For example, for the class Student, defined below, an instance of it would be 
   the information associated with a specific student.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is different from an instance attribute in that it is defined/set for all instances in a 
   class (though a specfic instance attribute can override the information set in a class attribute). For 
   example, in the class Student below, if all of our students go to the same school, we might set school =
   "Hackbright Academy," and this would be a class attribute, but if we wanted to specify that one student 
   attends somewhere else, by writing instance_name.school = "Balloonicorn Academy," this would be a instance 
   attribute.

"""

class Student(object):
	""" """
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
		if guess.lower() == self.correct_answer:
			return True
		else:
			return False

class Exam(object):
	""" """
	questions = []
	def __init__(self, name):
		self.name = name

	def add_question(self, question, correct_answer):
		question = Question(question, correct_answer)
		self.questions.append(question)

	def administer(self):
		score = 0
		for question in self.questions:
			if Question.ask_and_evaluate(question): 
				score += 1
		return score

class Quiz(Exam):
	""" """
	def add_question(self, question, correct_answer):
		super(Quiz, self).add_question(question, correct_answer)

	def administer(self):
		score = super(Quiz, self).administer()
		if float(float(score) / float(len(self.questions))) >= .5:
			return True
		else:
			return False

def take_test(exam, student):
	""" """
	student.score = Exam.administer(exam)
	return student.score

def example():
	""" """
	exam = Exam("Example Exam")
	exam.add_question("What is love?", "baby don't hurt me, don't hurt me, no more")
	exam.add_question("What is the best programming language?", "python, duh")
	exam.add_question("Yes or no--are these questions totally nonsensical?", "yes")
	example_student = Student("Talia", "Trilling", "123 Main ST")
	take_test(exam, example_student)


			




