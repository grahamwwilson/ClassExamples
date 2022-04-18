#!/bin/sh
# 
# Kill all python3 processs launched by me
#

uid=$(id -u $USER)
echo 'Found uid of '${uid}

ofile=processes.txt

ps -l | grep "$uid" | grep "python3" | cut -d " " -f6 > ${ofile}

for pid in $(cat ${ofile})
do
   kill -9 ${pid}
done

rm ${ofile}

exit
