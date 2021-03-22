# Coral DevBoard Setup
On Debian Linux 10 (Buster)

Screen
sudo apt install screen

Android Tools
Download from https://developer.android.com/studio/releases/platform-tools#downloads
mv ~/Download/fastboot ~/.local/bin
fastboot --version # verify it works from path

Mendel Development Tool
pip3 install --user mendel-development-tool

# Counting objects

#TODO Read and do https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/

sudo apt-get install libx11-dev libgtk-3-dev  
sudo apt-get install libopenblas-dev liblapack-dev  

Installing dlib in target environment  
https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/  
"Examples of object tracking algorithms include MedianFlow, MOSSE, GOTURN, kernalized correlation filters, and discriminative correlation filters, to name a few."


