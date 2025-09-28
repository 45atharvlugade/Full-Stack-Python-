from Demos.rastest import usage

input_=(input("Enter Any Value which should be intergral type----->  "))

def TryParse(s):
    try :
         return True , int(s)
    except ValueError:
        return False , None

ok , num=TryParse(input_)
if ok :
     print("Valid Number ")
else :
    print("Invalid Number ")