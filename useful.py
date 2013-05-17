#!/usr/bin/python
#Useful.py
#A container of useful methods.
import os;
try: input = raw_input;
except NameError: pass;
def hello():
   print ("Hello World!");

def HELPhello():
   print ('''
         Testing Hello World function, ensures this module
         is installed correctly.
         ''');

def get_files(directory):
   return [name for name in os.listdir(directory)
      if not os.path.isdir(os.path.join(directory, name))];

def HELPget_files():
   print ('''
         Generates a list of files in a given directory.
         Requires one argument, the given directory.
         ''');
         
def get_subs(directory):
   return [name for name in os.listdir(directory)
      if os.path.isdir(os.path.join(directory, name))];

def HELPget_subs():
   print ('''
         Generates a list of sub directories in a given directory.
         Requires one argument, the given directory.
         ''');

def ensure_dir(directory):
   directories = get_subs("../")
   if directory in directories:
      return True
   else:
      return False
      
def HELPensure_dir():
   print ('''
         Determines if a given directory already exists.
         Best when used along with mkdir function, to avoid
         overwriting existing directories. Also good to make
         sure a directory exists before you attempt to work in it.
         Requires one argument, the given directory.
         ''');

def mkdir(directory):
   os.makedirs(directory)

def HELPmkdir():
   print ('''
         Makes a directory matching the given argument. Requires a
         complete directory path ending in the new directory. Does
         not check to see if the directory already exists, may
         overwrite existing directories. Best used along with
         ensure_dir.
         Requires one argument, the given directory.
         ''');

def HELP():
   import useful;
   
   x = input("What can I do for you? (ListFunc/DefFunc/quit)\n: ")
   if x == "ListFunc":
      defaultFuncs = ['__cached__', '__initializing__', '__loader__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'useful', 'input']
      q = dir(useful)
      z = []
      for item in q:
         if item not in defaultFuncs and item[0:4] != "HELP":
            z.append(item);
      print (z);
      HELP();   
   elif x == "DefFunc":
      whatFunc = input("What function shall I define?\n");
      globals()["HELP"+whatFunc]();
      HELP();
   elif x == "quit":
      return;
   else:
      HELP();
if __name__ == "__main__":
   HELP();
