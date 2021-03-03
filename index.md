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
https://realpython.com/python-exceptions/
The above URL was useful because it had multiple examples and also explained the built-in exceptions.  It also had the following explanation of a try-except block:
	try:
		# run this code
	except:
		# execute this code when there is an exception

## Pickling
The pickle module can be imported and used to sterilize the data that is saved to a file.  The term unpickling effectively undoes this, or desterilizes, when reading from a file.  Sterilization effectively converts a data structure to stream of bytes.  The useful pickling functions are:
pickle.dump()
pickle.load()

A couple helpful websites for learning about pickling are:
https://realpython.com/python-pickle-module/
https://wiki.python.org/moin/UsingPickle
The above URLs were helpful because they explained sterilization in terms of the marshal, json, and pickle modules.  Both warned about raw pickle files and not to trust them if from an unknown source.

## Assignment
The assignment this week was to create a script that showcases pickling and exceptions.  To show pickling, I knew that I wanted to read and write from a file so I created a program that has saves journal entries with their date.  The user sees the past entries when the program starts, then asks for the date and new entry until the user types “exit” in the date field.  The dates and entries are pickled when written to the file and unpickled when reading from the file.  The try-except block was used to get around the EOFError (end of file)
Figure 1 shows the program running in PyCharm, Figure 2 shows pickling within functions and the try-except block, Figure 3 shows the main code, Figure 4 shows the program also running in the command line and adding and entry to what was already there, and finally Figure 5 shows the final resulting text file that has been pickled.








#####################################

You can use the [editor on GitHub](https://github.com/kirstencodes/IntroToProg-Python-Mod07/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/kirstencodes/IntroToProg-Python-Mod07/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
