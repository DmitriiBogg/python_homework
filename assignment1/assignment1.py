# Write your code here.
def hello():
    return "Hello!"

def greet (name):
    return f"Hello, {name}!"

def calc(a,b,operation ="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        else:
            return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        else:
            return f"Invalid type: {target_type}"
    except ValueError:
        return f"You can't convert {value} into a {target_type}."

def grade(*args):
    try:
        if not all(isinstance(x, (int, float)) for x in args):
            return "Invalid data was provided."
        average = sum(args)/len(args)
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        else:
            return "F"
    except Exception as e:
        return f"An error occurred: {e}"
    
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result
 # Join is faster actually )) lol.  sorry)) 

def student_scores(parameter, **kwargs):
    if not kwargs:
        return "No students provided!"
    if parameter == "best":
        return max(kwargs, key=kwargs.get)
    elif parameter == "mean":
        return round(sum(kwargs.values())/len(kwargs), 2) # a little hard question because didn't see a new words like len)) 
    return "Invalid parameter"

def titleize(string):
    words = string.split()
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    new_string = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            new_string.append(word.capitalize())
        elif word in little_words:
            new_string.append(word)
        else:
            new_string.append(word.capitalize())
    return " ".join(new_string) # this one was interesting
    
def hangman(secret, guess):
    words = []
    for letter in secret:
        if letter in guess:
            words.append(letter)
        else:
            words.append("_")
    return "".join(words) # a game from inro class))

def pig_latin(text):
    text = text.lower()
    words = text.split()
    vowels = "aeiou"
    result = []
    for word in words:
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
        elif word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1
            result.append(word[i:] + word[:i] + "ay")
    return " ".join(result)

# it was challenge )) a lot new command words and different commands