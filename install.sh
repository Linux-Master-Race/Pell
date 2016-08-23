echo "Pell Install Script"
read -p "Select bin directory: " bin
read -p "Select config directory: " config
echo "This script will not ascend to root, please do this yourself if either directory is not owned by yourself."

mkdir $config/src
cp -Rv src/* $config/src

echo "#!/bin/bash" > $bin/pell
echo "python $config/src/run.py" >> $bin/pell
chmod +x $bin/pell
