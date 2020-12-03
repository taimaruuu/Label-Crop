
if [ $# -lt 2 ];
then
    echo "Wrong amount of arguments given"
    echo "An input and output file must be given"
    echo "Ex: ./decrypt.sh input.pdf output.pdf"
    exit 1
else
    qpdf --decrypt --password= $1 $2
fi