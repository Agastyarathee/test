import os
def rename_files():
  # STEP-1: get all the file names from a folder.
  files = os.listdir("/content/sample_data")
  print(files)

  curr_dir = os.getcwd()
  print(curr_dir)

  os.chdir("/content/sample_data")
  print(os.getcwd())

  #STEP-2: for each file name rename it.
  for file_name in files:
    os.replace(file_name, file_name.translate(str.maketrans('','','1234567890')))

  files = os.listdir("/content/sample_data")
  print(files)

  os.chdir(curr_dir)

rename_files()