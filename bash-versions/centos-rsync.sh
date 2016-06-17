#!/bin/bash
# rsync from random CentOS repos, in order to host a mirror of CentOS repos
# can be done the same with epel, just change mirror_list and output
# array of geologicaly close CentOS mirrors to pull from
mirror_list=(rsync://mirror.us.oneandone.net/centos/ rsync://mirror.cs.pitt.edu/centos/ rsync://mirrors-pa.sioru.com/CentOS/ rsync://mirror.itc.virginia.edu/centos/ rsync://mirror.clarkson.edu/centos rsync://mirror.vcu.edu/centos/ rsync://mirror.umd.edu/centos/ )

#Generate and select a RANDOM Mirror from the list
RANDOM=$$$(date +%s)
ranMirror=${mirror_list[$RANDOM % ${#mirror_list[@]} ] }

echo "selected $ranMirror"

#do rsync of Delta from Mirrors
if [ -d /var/www/repo/html/CentOS/ ] ; then
     rsync -avSHP --delete --exclude "local*" --exclude "isos" --exclude "i386" \
         --exclude "i686" $ranMirror /var/www/repo/html/CentOS/
else
     echo "Target directory /var/www/repo/html/CentOS/ not present."
fi
#This will take a very long time, for the inital rsync but after that it just
# rsyncs the day to day changes or weekly, however you schedule it