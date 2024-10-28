#Q1
class HelloWorld:
    def greet1(self):
        print("hello world")

h = HelloWorld()
h.greet1()

#Q2
class Word:
    def __init__(self, _desc,_synonyms):
        self.desc=_desc
        self.synonyms=_synonyms

    def display(self):
        print("defination:", self.desc)
        print("synonyms:", ",".join(self.synonyms))

helloworld=Word("an expression of greeting",["hello","hi","howdy"])
helloworld.display()