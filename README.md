# first-project
## Environment
  MacBook Air Early 2014 Mac OS 10.13.6  
  Python 3.7.1  
  Anaconda 4.6.1  
  Tensorflow 1.12.0  
  OpenCV 3.4.2  

## Directory
./tensorflow  
|--/data  
|--/original_trainingdata  
|----/OK
|----/OK_test  
|----/NG  
|----/NG_test   
|--/test  
|----/OK  
|----/NG  
|--/training  
|----/OK  
|----/NG  
|--datatxt_org.py  
|--datatxt.py  
|--feature.py  
|--main.py  
|--model.py  
|--utils.py  
  
*/original_trainingdata/OK includes 131 items IMG_6753.JPG - IMG_7243.JPG  
*/original_trainingdata/OK_test includes 56 items IMG_7244.JPG - IMG_7299.JPG  
*/original_trainingdata/NG includes 132 items IMG_6947.JPG - IMG_6774.JPG  
*/original_trainingdata/NG_test includes 54 items IMG_6752.JPG - IMG_6998.JPG  

## Procedure
  1. Run feature.py  
    this create ORB/AKAZE feature into images from original_trainingdata  
    argument : training / test
  2. Run datatxt.py  
    this will move images with feature into training/test directory from original_trainingdata directory  
    additionally, data.txt (which is files path with labels and will be used at main.py) will be created on training/test directory as well  
    argument : training / test  
  3. Run main.py  
    this will create CNN model using training/test data  

## Notice
  main.py and model.py are referred/copied from those websites:  
  https://qiita.com/AkiyoshiOkano/items/72f3e4ba9caf514460ee  
  https://qiita.com/neriai/items/bd7bc36ec42c8ef65b2e  
