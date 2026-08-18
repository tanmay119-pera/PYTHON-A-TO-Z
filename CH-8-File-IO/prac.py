
# problem no 1 

'''create a new file "practice.txt using py.add the following data in it:

hi everyone 
we are learning file i/o
using java.
i like programming in java 

'''

with open("practice.txt","w") as f:
    f.write("hi everyone\nwe are learning file I/O\n")
    f.write("using java\ni like programming in java.\n")

# problem no 2 

'''waf that replaces all occurrences of "java" with "python" in above file'''

with open("practice.txt","r") as f: 
   data = f.read()

new_data = data.replace("java","python")
print("new_data")

with open("practice.txt","w") as f:
    f.write(new_data)

# problem no 3 

'''search if the word "learning" exists in the file or not.'''

def check_for_word():
   word = "xlearning"
   with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word)!= -1):
          print("found")
        else:
          print("not found")

# problem 4 

'''WAF to find in which line of the file does the word "learning" occur first.
print -1 if word not found. '''

def check_for_line():
    word = "learning"
    data = True
    line_no = 1 
    with open("practice.txt","r") as f:
       while data:
          data = f.readline()
          if (word in data):
             print(line_no)
             return 
          line_no += 1
    return -1 

check_for_line()

'''from  a file containing numbers separated by comma, print the count of even numbers. '''

with open("practice.txt","r") as f:
   data = f.read()
   print(data)

   num = ""
   for i in range(len(data)):
      if(data[i]==","):
         print(int(num))
         num = ""
      else:
         num += data[i]