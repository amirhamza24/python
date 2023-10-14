# rules: 1. directly module call kora
# import module
#
# module.createMod()

# rules: 2. module call kore sei module k arekta variable a rakha..
# import module as mod
#
# mod.createMod()
# mod.anotherMod1()
# mod.anotherMod2()
#
# print(mod.person1)  # ekta object k call kora hocche.

# rules 3. ekhane ekta ekta kore module call kore ante hobe
from module import createMod

createMod()