#!/bin/bash
# 
# Kill all python3 processs launched by me
#

uid=$(id -u $USER)
echo 'Found uid of '${uid}

ofile=processes.txt

ps -l | grep "$uid" | grep "python3" > ${ofile}

while read -r line
   do
      echo "$line"
      read -ra array <<<"$line"
      pid=${array[3]}
      echo 'Killing pid = '${pid}
      kill -9 ${pid}
   done < "$ofile"

rm ${ofile}

exit
