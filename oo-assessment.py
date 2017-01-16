"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Encapsulation - The data lives close to its functionality, meaning it is easy
   to read, debug, modify and test. Classes offer a breakdown of functionality
   that helps categorize where certain attributes belong in a project.

   Abstraction - Classes allow for complexity of a system to be "hidden away"
   from those reading the code that don't need to be bogged down in the details.
   If classes are imported into project code it can allow for faster debugging
   because the code is easier to read.

   Polymorphism - Classes are flexible and easily changeable. This is because
   classes offers the ability to assign class attributes, which you can easily
   override by an instance attribute where the attribute may not fit the
   specific instance created.

2. What is a class?

   A class is a category of objects that have shared methods or attributes.
   Creating a class allows for quick reusability of code for many instances of a
   similar object.

3. What is an instance attribute?

   An instance attribute refers to the specific attributes of the instance, or
   specific object, in question. An example would be the name (instance attribute)
   of a specific student at Hackbright (instance) who is female (class attribute).

4. What is a method?

   A method is a function within a class that is called using self as the first
   arguement (referring to the instance the method is being called on) and
   offers the ability to call some method that class can perform with the instance
   desired.

5. What is an instance in object orientation?

   An instance is the specific occurance of an object we are speaking of within
   a class. An example would be that Larry is an instance of the Cat class, and
   has his own instance attributes such as color and age, in addition to the class
   attributes like the ability to meow.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute would be referring to something that occurs most if not all
   the time in the objects associated with that class. An instance attribute is
   something that is specific to the exact instance of that class.

   If I make a class called Dog, a class attribute would be something most or all
   dogs have, such as a tail or the ability to speak. An instance attribute would
   be useful for talking about my own dog, by stating that Luna is in the Dog
   class and has cream and brown colored fur. This is not true for all or even
   most dogs, but it is true of the instance of Luna.


"""


class Student(object):
    """Student first names, last names and addresses"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A question and its answer are stored with this class"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        response = raw_input("%s > " % self.question)
        if response == self.answer:
            return True
        else:
            return False


class Exam(object):
    """Names an exam and adds questions onto it"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        self.questions.append(tuple(question, correct_answer))

    def take_exam(self):
        number_of_questions = 0
        correct = 0
        for problem in self.questions:
            answer = self.ask_question(problem)
            number_of_questions += 1
            if answer is True:
                correct += 1

        percentage = float(correct) / number_of_questions
        return percentage


def take_test(exam, student):
    """administer the test, add attribute to student instance of 'score' """
    pass


def example():
    pass

# I ran out of time to complete this assessment, I had a busy weekend planned
# and did not set aside enough time to focus. I will continue to work on these problems,
# but I wanted to make sure I got what I have submitted in time.

# My biggest issue is that I am still a bit slow on the practice side of learning
# how to make and use classes, so I will just need to spend more time working with
# them to get faster at understanding how to solve a problem with them.
