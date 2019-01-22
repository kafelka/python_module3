#Using try/except to give a clear error message
#f = open("testfile")
#errno 2 error


#try:
#    f = open("testfile")
#except Exception:
#    print("Error!")
    
   
#try:
#    f = open("testfile")
#except Exception:
#    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")


#try:
#    f = open("testfile.txt")
#except Exception:
#    print("Error!")

#multiple errors:
#try:
#    f = open('testfile.txt')
#    s1 = not_exists
#except Exception:
#    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")


#try:
#    f = open('testfile.txt')
#    s1 = not_exists
#except FileNotFoundError:
#    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")


#multiple exceptions
try:
    f = open('testfile.txt')
    s1 = not_exists
except FileNotFoundError:
    print("Sorry, this file does not exist, or the file name is wrong. Please double check.")
except Exception:
    print("Sorry, something is wrong after opening function.")

#ex1 print out exception as detected

#try:
#    f = open('testfile.txt')
#    s1 = not_exists
#except Exception as e:
#    print(e)
    
#system will print an actual error is there is something wrong in the try block
 
#ex2 else block

#try:
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#    
    
#ex3  finally block
#try:
#    f = open('testfile')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print("executing finally...")
    
#try:
#    f = open('testfile.txt')
#except Exception as e:
#    print(e)
#else:
#    print(f.read())
#    f.close()
#finally:
#    print("executing finally...")
    
try:
    f = open("testfile.txt")
    if f.name == "testfile.txt":
        raise Exception
except Exception as e:
    print("file names are the same")