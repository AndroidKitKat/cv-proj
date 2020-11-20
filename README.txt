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

NOTE: We had a great deal of trouble getting the SURF dependencies in order. The only
way we were able to do so was by asking a friend of ours who does CV research for his
Conda environment. We have attempted to trim as many unnecessary dependencies as we
can, but there are still quite a few dependencies, and attempting to remove more 
invariably breaks our project. We also are not certain if our conda environment will 
set up correctly on a Windows machine, as neither of us have access to one. We
apologize for any inconvenience caused by needing to download dependencies. If you
attempt to test this project on a Windows machine and it does not work, we again
apologize and have attached a video of us running the demo locally in hopes that such
a video would be a sufficient replacement. Here is a link to the video:

3. Run Python script

`python3 main.py`

To , you can download the final archive of all images with their best 
match from the internet. This archive is located at: 
https://www.michaeleisemann.com/assets/cv/fin_images.tar.gz

`curl https://www.michaeleisemann.com/assets/cv/fin_images.tar.gz > fin_images.tar.gz`

To extract the final data:

`tar -xzvf fin_images.tar.gz`
