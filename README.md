# first-project
## Environment
  MacBook Air Early 2014 Mac OS 10.13.6  
  Python 3.7.1  
  Anaconda 4.6.1  
  Tensorflow 1.12.0  
  OpenCV 3.4.2  

## Directory
./tesndowflow  
  /data  
  /original_trainingdata  
    /OK  
    /OK_test  
    /NG  
    /NG_test   
  /test  
    /OK  
    /NG  
  /training  
    /OK  
    /NG  
  datatxt_org.py  
  datatxt.py  
  feature.py  
  main.py  
  model.py  
  utils.py  
  
## Procedure
  1. Run feature.py  
    this create ORB/AKAZE feature into images  
    argument : training / test
  2. Run datatxt.py  
    this will move images with feature into training/test directory from original_trainingdata directory  
    additionally, data.txt (which is files path with labels and will be used at main.py) will be created on training/test directory as well  
    argument : training / test  
  3. Run main.py  
    this will create CNN model using training/test data  
