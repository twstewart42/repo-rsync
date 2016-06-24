# repo-rsync

Use this script to rsync remote repositories to a local yum/rpm server.

Uses the <a href="http://www.owlfish.com/software/utils/RSyncBackup"/>RSyncBackup python library</a> to conduct the rsyncing.

Python2.7


<pre>
/usr/local/bin/repo-rsync.py -h
usage: repo-rsync.py [-h] c

Python: rsyncs either CentOS or Epel repos to a local repository

positional arguments:
 c values: C, E

optional arguments:
 -h, --help show this help message and exit</pre>
<pre>#syncs centos
5 1 * * * python /usr/local/bin/repo-rsync.py C
#syncs Epel
25 20 * * 6 python /usr/local/bin/repo-rsync.py E
</pre>
&nbsp;
