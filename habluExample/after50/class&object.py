class studentList:
    name: ""
    number: ""


a = studentList()  # a ekta object.. ei a studentList class er sob property er access pabe..
b = studentList()  # b ekta object.. ei b o studentList class er sob property er access pabe..

a.name = "Rakib"
a.number = 1234564123
b.name = "Sakib"
b.number = 5235353543322

print(a.name)
print(a.number)
print(b.name)
print(b.number)