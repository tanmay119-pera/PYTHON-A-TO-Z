'''                                            FILES INPUT/OUTPUT                                                  '''


'''PYTHON  CAN BE USED TO PERFORM OPERATION ON A FILE. (read and write data)

1. THREE ESSENTIAL STEP.

Open: Connect your program to the file using the open() function.

Process: Read the existing data or write new data.

Close: Disconnect from the file to save your changes and free up computer memory.

2.THE "MODES"

'r' (Read): You just want to look at the data. You cannot change anything. (This is the default mode).

'w' (Write): You want to write data. Warning: If the file already has text in it, 
this mode will completely erase the old text and replace it with your new text. If the file doesn't exist, 
Python will create it for you.

'a' (Append): You want to add new data to the very end of the file without erasing what is already there.


3. While you can manually open and close files using file.close(),
 programmers usually use a with statement. It is a safety net that automatically closes the file for you as 
 soon as the block of code finishes running, even if an error crashes your program in the middle of it.

'''
#=====================================================================================================================================

''' TYPES OF ALL FILES 

1. TEXT FILES : .txt,.docx,.log etc. 

2. BINARY FILES : .mp4,.mov,.png,.jpeg etc.

'''

#========================================================================================================================================

''' open,read & close file 

f = open("file_name","mode")


sample.txt.            r: read mode
demo.docx              w: write mode 


data = f.read()
f.close()

'''

f = open("demo.txt","r") # to open a file 

data = f.read() # to read a file 
print(data)
print(type(data)) # data types 

f.close() # to close the file 

#=======================================================================================================================================
'''
=======================================================================================================================================
  CHARACTER     |                     MEANING                            SYNTAX
#=======================================================================================================================================  
             
   'r'             " open for reading (default) "                no truncate

#                                                                with open('example.txt', 'r') as file:
#                                                                content = file.read()
=======================================================================================================================================
   
   'r+'	          " Read and write. Raises I/O error if the
'                                     file does not exist. "      no truncate / pointer start 

#                                                                 with open('example.txt', 'r+') as file:
#                                                                 content = file.read()
#                                                                 file.write('\nThis is a new line.')
========================================================================================================================================

   'w'             " open for writing, truncating the file first.   truncate

#                                                                 with open('example.txt', 'w') as file:
#                                                                 file.write('Hello, world!')
========================================================================================================================================
   
   'w+'          " Read and write. Overwrites file or creates      truncate
'                   new one

#                                                                 with open('example.txt', 'w+') as file:
#                                                                 file.write('Hello, world!')
#                                                                 file.seek(0)
#                                                                 content = file.read()
========================================================================================================================================

   'x'             " create a new file and open it for writing "
#                                                                 with open("file.txt", "x") as f:
#                                                                 f.write("Hello World!")
=========================================================================================================================================
  
   'a'             " open for writing,appending to the end of     no truncate 
'                          the file if it exists "

#                                                                with open('example.txt', 'a') as file:
#                                                                file.write('\nThis is a new line.')
=========================================================================================================================================
   
   'a+'          " Read and append. Pointer at end. Creates      no truncate / pointer end
'                file if it doesn't exist. " 

#                                                               with open("file.txt", "a+") as f:
#                                                               f.write("New line added\n")  # Append
#                                                               f.seek(0)                    # Go to start
#                                                               print(f.read())              # Read all

========================================================================================================================================

   'b'             " binary mode "

#                                                               with open('image.png', 'rb') as file:
#                                                               data = file.read()
=========================================================================================================================================

   't'             " text mode (default)"

#                                                               with open("file.txt", "rt") as f:
#                                                               print(f.read())
==========================================================================================================================================

   '+'             " open a disk file for updating 
   '                  (reading and writing)

#                                                                with open("file.txt", "r+") as f:
#                                                                f.write("Updated!")  # Write
#                                                                f.seek(0)            # Go to start
#                                                                print(f.read())      # Read
==========================================================================================================================================
  
   'rb'          " Read in binary mode. File must exist. "

#                                                                with open("file.txt", "rb") as f:
#                                                                print(f.read())  # b'Hello World!'
===========================================================================================================================================

   'rb+'	         " Read and write in binary mode. File must exist."

#                                                                 with open("file.txt", "rb+") as f:
#                                                                 f.write(b"Hello!")  # Write bytes
#                                                                 f.seek(0)           # Go to start
#                                                                 print(f.read())     # b'Hello!'
===========================================================================================================================================

   'wb'          "  Write in binary. Overwrites or creates new."

#                                                                 with open("file.txt", "wb") as f:
#                                                                 f.write(b"Hello!")  # Write bytes
===========================================================================================================================================

   'wb+'         " Read and write in binary. Overwrites or creates new."

#                                                                  with open("file.txt", "wb+") as f:
#                                                                  f.write(b"Hello!")  # Write bytes
#                                                                  f.seek(0)           # Go to start
#                                                                  print(f.read())     # b'Hello!'
===========================================================================================================================================

   'ab'	        " Append in binary. Creates file if not exist."

#                                                                  with open("file.txt", "ab") as f:
#                                                                  f.write(b"New bytes!")  # Append bytes
===========================================================================================================================================

   'ab+'	        " Read and append in binary. Creates file if it does not exist. "

#                                                                  with open("file.txt", "ab+") as f:
#                                                                  f.write(b"New bytes!")  # Append bytes
#                                                                  f.seek(0)               # Go to start
#                                                                  print(f.read())         # Read all bytes
===========================================================================================================================================
'''
#===========================================================================================================================================

''' READING A FILE '''

#1. reads entire file 

f = open("demo.txt")
data = f.read()
f.close()

#2. reads some words

f = open("demo.txt")
data = f.read(7) # output : i am ir
f.close()

#3. reads one line at a time 

f = open("demo.txt")
data = f.readline()
f.close()

#or 

f = open("demo.txt","r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

#===============================================================================================================================================

''' WRITING A FILE '''


'''#overwrites the entire file

f = open("demo.txt","w")

f.write("this is a new line")''' 

f = open("demo.txt","w")
f.write("I want to learn python asap")
f.close()


'''#adds to the file

f = open("demo.txt","a")

f.write("this is a new line")'''

f = open("demo.txt","a")
f.write("\nthen I'll do java s")
f.close()

''' TO MAKE NEW FILE WHILE IN '''

f = open("sample.txt","w")
f.close()

f = open("sample.txt","a")
f.close()

#==========================================================================================================================================

''' WITH SYNTAX '''


with open("demo.txt","r")as f:
   data = f.read()
   print(data)


with open("demo.txt","w") as f:
   f.write("new data")

#===========================================================================================================================================
'''
 DELETING A FILE (USING THE OS MODULE)

module(like a code library) is a file written by another programmer that generally has a
function we can use.

import os 
os.remove(filename)
'''

import os 
os.remove("sample.txt")






