To be able to run this file be sure you have PyPDF2 installed.
To install run the following command:

conda install -c conda-forge pypdf2

Before being able to crop and rotate your label PDF it cannot be encrypted.
To check encryption status run the following:

qpdf --show-encryption -file_name-

To remove encryption use the decrypt.sh bash script provided. To run the script first permissions must be given 

chmod +x decrypt.sh

To run file use:

sh decrypt.sh
or
./decrypt.sh