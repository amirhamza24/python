import datetime

a = datetime.datetime.now()

print(a)  #ekhane date and time eksathe dekhabe
print(a.strftime("%a"))  # ekhane day er nam dekhabe short kore (Sun)
print(a.strftime("%A"))  # ekhane day er nam dekhabe full (Sunday)
print(a.strftime("%d"))  # ekhane shudhu aj koto tarikh seta dekhabe  
print(a.strftime("%m"))  # ekhane koto tomo mash seta dekhabe (October == 10)