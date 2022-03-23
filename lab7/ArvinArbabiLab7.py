'''
Class called Message that models a basic email application.

https://github.com/ArvinArbabi/Assignments/tree/master
'''

class Message:
    # Constants
    MAX_LEN = 50
    EMPTY = ""

    # A constructor with parameters self, sender and recipient.
    # Sets values for sender and recipient.
    # Sets body as an empty string.
    def __init__(self, sender, recipiant):
        self.str_ok(sender)
        self.str_ok(recipiant)
        self.sender = sender
        self.recipiant = recipiant
        self.body = self.EMPTY

    # Mutator - setting sender
    def set_sender(self, sender):
        self.str_ok(sender)
        self.sender = sender
    
    # Mutator - setting recipiant
    def set_recipiant(self, recipiant):
        self.str_ok(recipiant)
        self.recipiant = recipiant
    
    # A method append with parameters self and line.
    # Line contains the line of text to add to the body of the email message.
    # End each email message line with a newline character.
    def append(self, line):
        self.str_ok(self.body)
        self.body += line + "\n"
    
    # Clears the content of the email body
    def clear_body(self):
        self.body = self.EMPTY

    # A method to_string that returns a string representation of the entire message.
    # The entire message includes the sender, the recipient and the body of the message.    
    def toString(self):
        m = "From: {}\nTo: {}\n{}".format(self.sender,self.recipiant,self.body)
        return m

    # A helper method str_ok() that validates str parameters.
    def str_ok(self, value):
        if len(value) > self.MAX_LEN:
            raise ValueError("Invalid value: string must be less than 50 characters.")
# ========================================================
# From: Arvin
# To: self
# This year, I would like to:
# do 20 pullups
# hit 170 lbs

# From: Roham
# To: self
# For Turkey, I need:
# pants
 



