Notre Dame Computer Vision Fall 2020

Final Project -- Campus Building Recognizer

Matthew Siciliano and Michael Eisemann


-=-=-=-=-=-=-=-=-=-
|    S E T U P    |
-=-=-=-=-=-=-=-=-=-

1. Make "setup.sh" executable

`chmod +x setup.sh`

2. Run setup.sh
   This script downloads two datasets from the internet and configures an
   anaconda environment with the right dependencies. 

`./setup.sh`

   Make sure you activate the anaconda environment!

3. Run Python script
   This script will attempt to test all the unknown images against the training
   data to find the best result. This is a very lengthy process even with a
   moderately powered CPU. For reference, it took ~5 hours on a Core i7-7700k

`python3 verify.py`

To save time, you can download the final archive of all images with their best 
match from the internet. This archive is located at: 
https://www.michaeleisemann.com/assets/cv/fin_images.tar.gz

`wget https://www.michaeleisemann.com/assets/cv/fin_images.tar.gz`

To extract the final data:

`tar -xzvf fin_images.tar.gz`
