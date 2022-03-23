'''
Class called Message that models a basic email application.

https://github.com/ArvinArbabi/Assignments/tree/master
'''

class Message:
    # Constants
    MAX_LEN = 50
    EMPTY_STR = ""

    # A constructor with parameters self, sender and recipient.
    # Sets values for sender and recipient.
    # Sets body as an empty string.
    def __init__(self, sender, recipiant):
        self.str_ok(sender)
        self.str_ok(recipiant)
        self.sender = sender
        self.recipiant = recipiant
        self.body = self.EMPTY_STR

    def set_sender(self, sender):
    ## Sets sender of the message
    # Validates parameter else sets to default
    #  @param sender
    #  @return Boolean 
        if self.str_ok(sender):  # requires helper method to validate string
            self.sender = sender
            return True
        self.sender = self.EMPTY_STR 
        return False 

    # Mutator - setting recipiant
    def set_recipiant(self, recipiant):
    ## Sets recipiant of the message
    # Validates parameter else sets to default
    #  @param recipiant
    #  @return Boolean 
        if self.str_ok(recipiant):  # requires helper method to validate string
            self.recipiant = recipiant
            return True
        self.recipiant = self.EMPTY_STR 
        return False 

    # A method append with parameters self and line.
    # Line contains the line of text to add to the body of the email message.
    # End each email message line with a newline character.
    def append(self, line):
        if self.str_ok(line):  # requires helper method to validate string
            self.body += line + "\n"
            return True
        self._sender = self.EMPTY_STR 
        return False 
        
    
    # Clears the content of the email body
    def clear_body(self):
        self.body = self.EMPTY_STR

    # A method to_string that returns a string representation of the entire message.
    # The entire message includes the sender, the recipient and the body of the message.    
    def toString(self):
        m = "From: {}\nTo: {}\n{}".format(self.sender,self.recipiant,self.body)
        return m

    # A helper method str_ok() that validates str parameters.
    
    def str_ok(self, value):
        return len(value) <= self.MAX_LEN
            
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
 



