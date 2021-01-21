with open('session.log') as file_object:
    lines=file_object.readlines()

string1=' '
for line in lines:
    string1 += line.strip()

print(string1.strip())
print('this is tset 1')