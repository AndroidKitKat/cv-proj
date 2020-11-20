#!/bin/sh

check_tools() {
    if ! [ -x "$(command -v curl)" ]; then
        echo "This script relies on curl. Please make sure it is installed and in your path!"
        exit 1
    fi
    
    if ! [ -x "$(command -v conda)" ]; then
        echo "This project relies on anaconda. Please make sure it is installed and in your path!"
        exit 1
    fi
}

check_and_download() {
    if ! [ -d "mass_data" ]; then
        echo "Making data storage folders..."
        mkdir "mass_data"
    fi

    # download the unknown data from my server...
    if ! [ -e "/tmp/Unknown.zip" ]; then
        echo "Downloading unknown set from the internet..."
        curl -v "https://www.michaeleisemann.com/assets/cv/Unknown.zip" > /tmp/Unknown.zip
    fi

    # download the traning data from my server...
    if ! [ -e "/tmp/Training.zip" ]; then
        echo "Downloading training data set from the internet..."
        curl -v "https://www.michaeleisemann.com/assets/cv/Training.zip" > /tmp/Training.zip
    fi    
}

extract_the_stuff() {
    unzip -d "./mass_data" "$1"
}

check_tools
check_and_download
extract_the_stuff "/tmp/Unknown.zip"
extract_the_stuff "/tmp/Training.zip"

# set up anaconda
conda env create --file=billdings.yaml

echo "please activate the new conda environment by typing:"
echo "conda activate billdings"