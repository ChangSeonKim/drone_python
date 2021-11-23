a=10
b = 0
try :
    c= a/b
    
except ZeroDivisionError:
    c = a/1
except Exception:
    pass    
print(c)