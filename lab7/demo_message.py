##
#  Demonstrate the Message class.
#
from ArvinArbabiLab7 import Message

# Create the message.
wishList = Message("Arvin", "Self")
wishList.append("This year, I would like to:")
wishList.append("do 20 pullups")
wishList.append("hit 170 lbs")

# Display its contents.
print(wishList.toString())
wishList.set_sender("Roham")
wishList.clear_body()
wishList.append("For Turkey, I need:")
wishList.append("pants")
print(wishList.toString())