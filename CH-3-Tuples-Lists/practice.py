# Wap to ask user to enter 3 of their favorite movies and store them in a list. Then, print the list of movies.

movies = []
mov1 = input("Enter your first favorite movie: ")
mov2 = input("Enter your second favorite movie: ")
mov3 = input("Enter your third favorite movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Your favorite movies are: ", movies)

#================================================================================================================================

# Wap to check if the list contain a palindrome or not. [1,"abc","abc",1]    

''' first method '''
list2 = [1, "abc", "abc", 1]
copy_list2 = list2.copy()
copy_list2.reverse()
if list2 == copy_list2:
    print("The list is a palindrome.")
else: 
    print("The list is not a palindrome.") 



''' set(iterable)'''
def is_palindrome(lst):
    return lst == lst[::-1]

numbers = [1, "abc", "abc", 1]
if is_palindrome(numbers):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

#================================================================================================================================

# Wap to count the number of students with the "A" grade in following tuple.add()
#["C","D","A","A","B","B","A"]  

grades = ("C", "D", "A", "A", "B", "B", "A")
count_a = grades.count("A")
print("Number of students with 'A' grade:", count_a)  


# store the above value in a list and sort them "A" TO "D" and print the sorted list.
grade_list = list(grades)
grade_list.sort()
print("Sorted grades:", grade_list)

#=================================================================================================================