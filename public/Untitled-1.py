

def recitation1():
        # List comprehension
    # squares = [x**2 for x in range(10)]
    # print(squares)

    words = ["hi", "my", "name", "is", "Ephraim"]
    # squares = [x[0] for x in words]
    # print(squares)

    # Generator expressions

    # gen = (n**2 for n in range(5))
    # print(next(gen), next(gen), next(gen), next(gen), next(gen))

    # Classes


    #this isn't working exactly... will fix later
    class Incrementer:
            #method that will get called when incrementer is called
            def __init__(self, initial_count: int) -> None:
                #self is a reference to the object we're creating.
                self.count = initial_count
            def increment(self, n):
                self.count += n
            def decrement(self, n):
                self.count -= n
        
    # incrementer = Incrementer(5)
    # print(incrementer) # reference to it

    # print(incrementer.count) # reference to it


    # Default arguments

    def join_strings_hyphen(strings):
        return '-'.join(strings)
    print(join_strings_hyphen("abc")) #a-b-c


    def join_string(strings, sep="-"): #the latter is a default argument 
        return sep.join(strings)
    print(join_string("abc")) #a-b-c

    def a_plus_b_plus_c(a, b=1, c=2):
        return (a + b) * c

    print(a_plus_b_plus_c(1, 2, 3)) # 9
    print(a_plus_b_plus_c(1, b=2, c=3)) # 9 
    print(a_plus_b_plus_c(1, c=2, b=3)) # 8 
    # *args are worth looking up



def recitation2():
    # #Classification methods
    # print("")
    # from collections import Counter
    # from sklearn.metrics import accuracy_score
    # import random

    # # Let's create a list of true classes where p(positive) = 0.99
    # n = 10000 # sample size
    # true_classes = ["positive" if random.random() < 0.99 else "negative" for _ in range(n)]

    # # Clearly, "positive" is now the most common class
    # Counter(true_classes)  
    # Counter({'positive': 9899, 'negative': 101})

    # #underscore is used as var not referenced
    # non spam emails are called ham

    test = ["Hello" for _ in range(5)]
    print(test)


# recitation2()















