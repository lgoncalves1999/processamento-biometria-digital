import os.path
from os import path

UPLOAD_FOLDER = './database'

def main():

   print ("file exist:"+str(path.exists('./database/comparacao.png')))
   print ("File exists:" + str(path.exists(UPLOAD_FOLDER + 'career.guru99.txt')))
   print ("directory exists:" + str(path.exists(UPLOAD_FOLDER + 'myDirectory')))

if __name__== "__main__":
   main()