#!/bin/bash

declare -a SOURCES

BUILD_FOLDER="build"
BUILD_ZIP="$BUILD_FOLDER/extension.zip"
SOURCES=("fix.css" "manifest.json")

add_padding() {
    local line=""
    while read -d $'\n' line 
    do
        echo "    $line" 
    done
}

if [ -f build ];
then
    mkdir build
    echo "Folder 'build' created successfully"
else
    echo "Folder 'build' already exists"
fi

echo "Building:"
IFS=' ' zip $BUILD_ZIP ${SOURCES[*]} | add_padding
echo "Created '$BUILD_ZIP' successfully."