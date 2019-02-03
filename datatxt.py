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
  org_dir_path_ok ='./original_trainingdata/OK/'
  org_dir_path_ng ='./original_trainingdata/NG/'
elif arg[1] == 'test':
  #test
  new_dir_path_ok ='./test/OK/'
  new_dir_path_ng ='./test/NG/'
  org_dir_path_ok ='./original_trainingdata/OK_test/'
  org_dir_path_ng ='./original_trainingdata/NG_test/'
else:
  print('arg should be training or test')
  sys.exit()

os.makedirs(new_dir_path_ok, exist_ok=True)
os.makedirs(new_dir_path_ng, exist_ok=True)

org_dir_path_ok_files = os.listdir(org_dir_path_ok)
org_dir_path_ng_files = os.listdir(org_dir_path_ng)

movecntok = 0
movecntng = 0

#OK picutres with ORG feature will move to newdir
for ok_orgimg_file in org_dir_path_ok_files:
  ok_orgfilepath = org_dir_path_ok + ok_orgimg_file
  if ok_orgimg_file.find('_OK') > 0:
    shutil.move(ok_orgfilepath, new_dir_path_ok)
    movecntok += 1
  else:
    print('This file :' + ok_orgimg_file + ' is not moved')
if movecntok == 0:
    print('No file to move, terminate this process')
    sys.exit()

#NG picutres with ORG feature will move to newdir
for ng_orgimg_file in org_dir_path_ng_files:
  ng_orgfilepath = org_dir_path_ng + ng_orgimg_file
  if ng_orgimg_file.find('_NG') > 0:
    shutil.move(ng_orgfilepath, new_dir_path_ng)
    movecntng += 1
  else:
    print('This file :' + ng_orgimg_file + ' is not moved')
if movecntng == 0:
    print('No file to move, terminate this process')
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
