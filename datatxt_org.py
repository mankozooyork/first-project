import os
import os.path
import shutil
import sys

# move pictures with ORB feature to new directory from original direcotry
# then create data.txt which contains abosolute path with class label
# finally move data.txt to ./test folder

arg = sys.argv
print(arg)

if arg[1] == 'training':
  #training
  new_dir_path_ok ='./training/OK/'
  new_dir_path_ng ='./training/NG/'
elif arg[1] == 'test':
  #test
  new_dir_path_ok ='./test/OK/'
  new_dir_path_ng ='./test/NG/'
else:
  print('arg should be training or test')
  sys.exit()

pos_orgimg_dir = new_dir_path_ok
pos_orgimg_files = os.listdir(pos_orgimg_dir)

neg_orgimg_dir = new_dir_path_ng
neg_orgimg_files = os.listdir(neg_orgimg_dir)

for pos_orgimg_file in pos_orgimg_files:
  pos_orgfilepath = pos_orgimg_dir + pos_orgimg_file
  # not include hidden files
  root, ext = os.path.splitext(pos_orgfilepath)
  if ext == ".JPG" :
    #print(neg_orgfilepath)
    abpath = os.path.abspath(pos_orgfilepath)
    print(abpath)
    f = open('data.txt','a')
    pos_filepath_withlabel = abpath + ' 0' + '\n'
    f.write(pos_filepath_withlabel)

for neg_orgimg_file in neg_orgimg_files:
  neg_orgfilepath = neg_orgimg_dir + neg_orgimg_file
  # not include hidden files
  root, ext = os.path.splitext(neg_orgfilepath)
  if ext == ".JPG" :
    #print(neg_orgfilepath)
    abpath = os.path.abspath(neg_orgfilepath)
    print(abpath)
    f = open('data.txt','a')
    neg_filepath_withlabel = abpath + ' 1' + '\n'
    f.write(neg_filepath_withlabel)

f.close()
os.system('cat data.txt | sort -R >data-ramdom.txt')
os.system('rm data.txt')

if arg[1] == 'training':
  shutil.move('./data-ramdom.txt', './training/')
elif arg[1] == 'test':
  shutil.move('./data-ramdom.txt', './test/')
else:
  print('data-ramdom.txt is not moved')
