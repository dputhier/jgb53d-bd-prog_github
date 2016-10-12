#!/bin/bash															
# The line above tells the system that the code should be interpreted
# by the bash shell, which is located in /bin directory.

wget https://github.com/arq5x/bedtools2/archive/master.zip			# Download bedtools
unzip master.zip             # Uncompress the archive
mkdir -p  ~/soft             # Create a directory named 'soft' in your home directory 
mv bedtools2-master ~/soft   # move bedtools2-master directory to ~/soft
cd ~/soft/bedtools2-master   # Change working directory to ~/soft/bedtools2-master
make                         # Compile the program
echo "export PATH=$PATH:~/soft/bedtools2-master/bin" >> ~/.bashrc	# Add a new line to ~/.bashrc 
source ~/.bashrc             # Tell the terminal to reload the  ~/.bashrc
