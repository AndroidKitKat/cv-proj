Notre Dame Computer Vision Fall 2020

Final Project -- Campus Building Recognizer

Matthew Siciliano and Michael Eisemann


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
|    D E P E N D E N C I E S    |
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

anaconda: https://www.anaconda.com
curl

-=-=-=-=-=-=-=-=-=-
|    S E T U P    |
-=-=-=-=-=-=-=-=-=-

1. Download the .zip file from this repository, unzip it, and navigate to the 
`cv-proj-master` directory in anaconda.

2. Setup the anaconda environment

`conda env create --file=billdings.yaml`

3. Run Python script

`python3 main.py`

To , you can download the final archive of all images with their best 
match from the internet. This archive is located at: 
https://www.michaeleisemann.com/assets/cv/fin_images.tar.gz

`curl https://www.michaeleisemann.com/assets/cv/fin_images.tar.gz > fin_images.tar.gz`

To extract the final data:

`tar -xzvf fin_images.tar.gz`
