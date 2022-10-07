#!/bin/tcsh

### Replace the following lines according to your setup.
set EXEC=/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis
set OUTPUT=/eos/home-a/antoniov/SWAN_projects/pps-ww-analysis/output
###

#set file=$1
#set label=$2
#set option1="$3"
#set option2="$4"
#set option3="$5"
#set option4="$6"
#set option5="$7"
#set option6="$8"
#echo "file: "$file
#echo "label: "$label
#echo "option: "$option1
#echo "option: "$option2
#echo "option: "$option3
#echo "option: "$option4
#echo "option: "$option5
#echo "option: "$option6

echo $EXEC
echo $OUTPUT

set currentdir=`pwd`
cd $EXEC
echo $EXEC
source set_cmssw.csh
cd $currentdir
echo $currentdir
ls

if ( ! $?PYTHONPATH ) then
    if ( ! $?PYTHON3PATH ) then
        setenv PYTHONPATH ${EXEC}
        echo "PYTHONPATH set to $PYTHONPATH"
    else
        setenv PYTHON3PATH ${PYTHON3PATH}:${EXEC}
        echo "PYTHON3PATH set to $PYTHON3PATH"
    endif 
else
    setenv PYTHONPATH ${PYTHONPATH}:${EXEC}
    echo "PYTHONPATH set to $PYTHONPATH"
endif
env

echo 'Running...'
echo python3 $EXEC/process_data_random_protons_single_arm.py
python3 $EXEC/process_data_random_protons_single_arm.py
cp *.h5 $OUTPUT
