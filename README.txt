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

2. Setup the anaconda environment:

`conda env create --file=billdings.yaml`

NOTE: We had a great deal of trouble getting the SURF dependencies in order. The only
way we were able to do so was by asking a friend of ours who does CV research for his
Conda environment. We have attempted to trim as many unnecessary dependencies as we
can, but there are still quite a few dependencies, and attempting to remove more 
invariably breaks our project. We also are not certain if our conda environment will 
set up correctly on a Windows machine, as we developed our project on MacOS (although 
we think it should). We apologize for any inconvenience caused by needing to download 
dependencies. If you attempt to test this project on a Windows machine and it does not 
work, we again apologize and have attached a video of us running the demo locally in 
hopes that such a video would be a sufficient replacement. Here is a link to the video:
https://youtu.be/5lbeivUn7KQ 

3. Activate the anaconda environment:

`conda activate billdings`

4. To run our project, run the included Python script. This should take less than 30
seconds. Note that we included a small subset of our database for this demo in order
to speed up run time.

`python3 main.py`

5. When the result is determined, the best-match image name and the number of keypoint
matches found will be printed to the terminal. There will also be an image saved to the
working directory displaying the keypoint matches between the test image (left) and the
image found to be its nearest match.

Bonus:
You can download an archive containing all of our results (processed images) from 
the internet. This archive is located at: 
https://www.michaeleisemann.com/assets/cv/fin_images.tar.gz

To download the archive:
`curl https://www.michaeleisemann.com/assets/cv/fin_images.tar.gz > fin_images.tar.gz`

To extract our results from the downloaded archive:
`tar -xzvf fin_images.tar.gz`
