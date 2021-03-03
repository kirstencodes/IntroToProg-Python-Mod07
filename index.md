### Kirsten Elghoroury
### Foundations of Programming: Python (IT FND 110B)
### Assignment 07
### March 2, 2021
### GitHub Page: https://github.com/kirstencodes/IntroToProg-Python-Mod07 
### Website: https://kirstencodes.github.io/IntroToProg-Python-Mod07/ 

# Exceptions and Pickling

This week I learned about how to work with exceptions (such as try-except) as well as the pickle module that is used for text sterilization.  I also learned more about creating a GitHub webpage and the formatting of it.

## Exceptions
Exceptions are a great way to let the user know that there is an error in the program based on something they have input, giving them helpful instructions in laymen’s terms on why that is the case.  The developer should assume that the user will make some errors, so this is a way to catch what those might be.  There are many built-in exceptions such as ZeroDivisionError, but you can also make your own.  A common way to create your own is the try-except block.  
A helpful website for learning about exceptions was:
[This link](https://realpython.com/python-exceptions/)
The above URL was useful because it had multiple examples and also explained the built-in exceptions.  It also had the following explanation of a try-except block:
```markdown
	try:
		# run this code
	except:
		# execute this code when there is an exception
```

## Pickling
The pickle module can be imported and used to sterilize the data that is saved to a file.  The term unpickling effectively undoes this, or desterilizes, when reading from a file.  Sterilization effectively converts a data structure to stream of bytes.  The useful pickling functions are:
```markdown
pickle.dump()
pickle.load()
```

A couple helpful websites for learning about pickling are:
[This link](https://realpython.com/python-pickle-module/)
[This link](https://wiki.python.org/moin/UsingPickle)
The above URLs were helpful because they explained sterilization in terms of the marshal, json, and pickle modules.  Both warned about raw pickle files and not to trust them if from an unknown source.

## Assignment
The assignment this week was to create a script that showcases pickling and exceptions.  To show pickling, I knew that I wanted to read and write from a file so I created a program that has saves journal entries with their date.  The user sees the past entries when the program starts, then asks for the date and new entry until the user types “exit” in the date field.  The dates and entries are pickled when written to the file and unpickled when reading from the file.  The try-except block was used to get around the EOFError (end of file)
Figure 1 shows the program running in PyCharm, Figure 2 shows pickling within functions and the try-except block, Figure 3 shows the main code, Figure 4 shows the program also running in the command line and adding and entry to what was already there, and finally Figure 5 shows the final resulting text file that has been pickled.

![image](https://user-images.githubusercontent.com/79127964/109749698-025ba680-7b90-11eb-9477-dd744a131c0c.png)

Figure 1: In PyCharm, displaying previous entries when program is opened and asking for new entries.

![image](https://user-images.githubusercontent.com/79127964/109749775-25865600-7b90-11eb-848f-1976405734fe.png)

Figure 2: In PyCharm, code for defining functions including pickling and unpickling.

![image](https://user-images.githubusercontent.com/79127964/109749856-477fd880-7b90-11eb-9271-f2b039b868f7.png)

Figure 3: In PyCharm, main code displaying previous entries and while loop that asks for new entries until the user types “exit”.

![image](https://user-images.githubusercontent.com/79127964/109749865-4cdd2300-7b90-11eb-86e1-633e64d92296.png)

Figure 4: In the command line, the program still works as expected.

![image](https://user-images.githubusercontent.com/79127964/109749888-5070aa00-7b90-11eb-9827-f789c9d48112.png)

Figure 5: The resulting text file that shows the pickled entries.

## Summary
This week, I learned all about pickling as well as exception handling by writing a program that collects pickled journal dates and entries and allows the user to add entries to the file.
