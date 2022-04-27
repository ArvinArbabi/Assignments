import re
# pattern = "research"
# user_input = input()
# if(re.search(pattern, user_input)):
#     print("research")
# else:
#     print("not research")

# pattern = "(\d\d\d)-(\d\d\d)-(\d\d\d\d)"
# new_pattern = r"\1\2\3"
# user_input = input()
# new_user_input = re.sub(pattern, new_pattern, user_input)
# print(new_user_input)

pattern = "research"
string = "research arvin gabo research reza Research researchresearch"
print(len(re.findall(pattern, string, re.IGNORECASE)))

