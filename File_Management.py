import time
import os
import socket
import psutil
from datetime import datetime
import shutils
print("""
███╗░░░███╗██╗███╗░░██╗██╗░ █████╗░░██████╗
████╗░████║██║████╗░██║██║ ██╔══██╗██╔════╝
██╔████╔██║██║██╔██╗██║██║ ██║░░██║╚█████╗░
██║╚██╔╝██║██║██║╚████║██║ ██║░░██║░╚═══██╗
██║░╚═╝░██║██║██║░╚███║██║ ╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝ ░╚════╝░╚═════╝░""")
print("""
[1] Continue with setup
[2] I have already Done Setup""" )
setup=input("Enter choice[?]:")
if setup == '1':
      username=input(str("Please enter your name to be displayed:"))
      password=input(str("please enter your password to login:"))
      with open("E:\\username.txt",'w') as f:
            f.writelines(username)

      with open('E:\\password.txt','w') as f:
            f.writelines(password)
      print("Setup Complete!!!")
      input("Press Enter to close the window:")
if setup=='2':
      login_pass=open("E:\\password.txt")
      login_name=open("E:\\username.txt")
      l_p=login_pass.read()
      l_n=login_name.read()

while (True):
      l_p="buvi@123"
      login=input(str("please Enter the password to operating system:"))
      if login==l_p:
            #os.startfile(input())
            print("Correct password")
            print("******************\n")
            print("PERMISSION GRANTED")
            print("*******************")
            battery = psutil.sensors_battery()
            curr=datetime.now()
            print("Today's Date Is:" + time.strftime("%m/%d/%y"))
            print("Current Time Is:"+curr.strftime("%H:%M:%S"))
            print("The Battery Level is:")
            print(battery.percent)

            break
      elif(login!=l_p):

            print("Wrong password!")
while(True):
      print("***_______***_______***\n")
      print(""" 
      [0]--current working directory
      [1]--creating an root directory
      [2]--creating an folders 
      [3]--removing an directory
      [4]--changing an directory
      [5]--move the files
      [6]--exit
      """)
      print("***_______***_______***")
      user_input=input("Choose work[?]::")

      if user_input=='0':
          directory = os.getcwd()
          print("current working directory")
          print("------------------------\n")
          print(directory)
          print("-------------------------\n")
          print("successfully printed")
      elif user_input=='1':
          print("Creating an simple parent directory")
          dir = "D:/MINI_PROJECT"
          os.mkdir(dir)
          print("******************************\n")
          print("Parent Folder successfully created")
          print("*******************************")
      elif user_input=='2':
          while (True):
              print("""
                  [01]--Create an Video Format file
                  [02]--Create an Audio Format file
                  [03]--Create an Text Format file
                  [04]--Create an Image Format file
                  [05]--Create an Program Format file
                  [06]--Create an document Format file
                  [07]--Create an dataset Format file""")
              print("--------------------------------\n")
              creation = input("Enter your folder format:")
              print("----------------------------------")
              if (creation == '01'):
                  parent_dir = "D:\MINI_PROJECT"
                  folder = "VIDEO"
                  path = os.path.join(parent_dir, folder)
                  print(path)
                  if not os.path.exists(path):
                      os.makedirs(path)
                      print("Video Folder Created")
                      break
                  else:
                      print("Folder already exists")
              elif (creation == '02'):
                  parent_dir = "D:\MINI_PROJECT"
                  folder = "AUDIO"
                  path = os.path.join(parent_dir, folder)
                  print(path)
                  if not os.path.exists(path):
                      os.makedirs(path)
                      print("Audio Folder Created")
                      break
                  else:
                      print("Folder already exists")
              elif (creation == '03'):
                  parent_dir = "D:\MINI_PROJECT"
                  folder = "TEXT"
                  path = os.path.join(parent_dir, folder)
                  print(path)
                  if not os.path.exists(path):
                      os.makedirs(path)
                      print("Text Folder Created")
                      break
                  else:
                      print("Folder already exists")
              elif (creation == '04'):
                  parent_dir = "D:\MINI_PROJECT"
                  folder = "IMAGE"
                  path = os.path.join(parent_dir, folder)
                  print(path)
                  if not os.path.exists(path):
                      os.makedirs(path)
                      print("Image Folder Created")
                      break
                  else:
                      print("Folder already exists")
              elif (creation == '05'):
                  parent_dir = "D:\MINI_PROJECT"
                  folder = "PROGRAM"
                  path = os.path.join(parent_dir, folder)
                  print(path)
                  if not os.path.exists(path):
                      os.makedirs(path)
                      print("Program Folder Created")
                      break
                  else:
                      print("Folder already exists")
              elif (creation == '06'):
                  parent_dir = "D:\MINI_PROJECT"
                  folder = "DOCUMENT"
                  path = os.path.join(parent_dir, folder)
                  print(path)
                  if not os.path.exists(path):
                      os.makedirs(path)
                      print("Document Folder Created")
                      break
                  else:
                      print("Folder already exists")
              elif (creation == '07'):
                  parent_dir = "D:\MINI_PROJECT"
                  folder = "DATASETS"
                  path = os.path.join(parent_dir, folder)
                  print(path)
                  if not os.path.exists(path):
                      os.makedirs(path)
                      print("Dataset Folder Created")
                      break
                  else:
                      print("Folder already exists")

      elif user_input=='3':
          source = "D:\MINI_PROJECT"
          audio_files = "D:\MINI_PROJECT\VIDEO"
          video_files = "D:\MINI_PROJECT\AUDIO"
          image_file = "D:\MINI_PROJECT\IMAGE"
          programming_files = "D:\MINI_PROJECT\PROGRAMMING"
          text_files = "D:\MINI_PROJECT\TEXT"
          dataset_files = "D:\MINI_PROJECT\DATASET"
          document_files = "D:\MINI_PROJECT\DOCUMENTS"

          files = os.listdir(source)

          audio_formats = ['mp3', 'wav']
          doc_formats = ['doc', 'docx']
          text_formats = ['txt']
          video_formats = ['mp4', 'mkv']
          programming_formats = ['py', 'js', 'cpp', 'java']
          image_formats = ['jpg', 'jpeg', 'png']
          dataset_formats = ['csv']

          for file in files:
              file_ext = file.split(".")[-1]

              if file_ext in audio_formats:
                  shutils.move(file, audio_files)
              if file_ext in doc_formats:
                  shutils.move(file, document_files)
              if file_ext in video_formats:
                  shutils.move(file, video_files)
              if file_ext in text_formats:
                  shutils.move(file, text_files)
              if file_ext in programming_formats:
                  shutils.move(file, programming_files)
              if file_ext in image_formats:
                  shutils.move(file, image_files)
              if file_ext in dataset_formats:
                  shutils.move(file, dataset_files)
          print("*********************************************\n")
          print("SUCCESSFULLY MOVED TO  ITS CORRESPONDING FILES")
          print("**********************************************")

      elif user_input=='6':
          print("**********************************\n")
          print("EXIT...THANK U FOR MAKE USE OF IT")
          print("************************************")
          break
















