import os

# print(dir(os))# prints all the os module functions 
# print(os.getcwd())#prints the current working directory
# os.chdir("/Users/syedrihaanshah")#changes to directory 
# os.mkdir('test.txt')#makes a directory 
# os.makedirs('test/ex1')#makes a depper directory . Makes the parent directroy if it doesnt exist 
# os.rmdir('test')#removes the directory
# os.removedirs('test/ex1')#removes all directortys and sub dirs
# os.rename('test.txt', 'test-1.txt')#renames the directory or file 
# print(os.stat('test-1.txt/test.txt'))#os.stat() returns detailed metadata (statistics) about a file or directory.


print(os.listdir())
print(os.getcwd())