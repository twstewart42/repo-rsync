#!/usr/bin/python
import os
import random
import argparse
import RSyncBackup

def _rsync(Choice):
	rchoice = Choice
	if rchoice == 'C':
		print "Choice was CentOS"
		mirror_list = ['rsync://mirror.us.oneandone.net/centos/', 'rsync://mirror.cs.pitt.edu/centos/', 'rsync://mirrors-pa.sioru.com/CentOS/', 'rsync://mirror.itc.virginia.edu/centos/', 'rsync://mirror.clarkson.edu/centos', 'rsync://mirror.vcu.edu/centos/', 'rsync://mirror.umd.edu/centos/' ]
		local_dir = '/var/www/repo/html/CentOS/'
		ranMirror = random.choice(mirror_list)
		print 'selected %s' % ranMirror
		exclude = ['local*', 'isos', 'i386', 'i686']
	elif rchoice =='E':
		print "Choice was Epel"
		mirror_list = ['rsync://mirror.unl.edu/fedora-epel', 'rsync://mirror.cs.pitt.edu/fedora-epel', 'rsync://mirrors.mit.edu/fedora-epel']
	        local_dir = '/var/www/repo/html/EPEL/'
        	ranMirror = random.choice(mirror_list)
	        print 'selected %s' % ranMirror
        	exclude = ['local*', 'isos', 'i386', 'i686', '4', 'ppc64', 'debug']
	else:
		print "No choice was made"
		sys.exit()

	if os.path.exists(local_dir) == True:
		print 'true'
		backup = RSyncBackup.RSyncBackup(lastRunFile = '/tmp/centos-rsync', rsync="/usr/bin/rsync")
		backup.backup(source=ranMirror, destination=local_dir, excludeList=exclude)
		#rsync("-avSHP", "--delete", "--exclude=local*", "--exclude=isos", "--exclude=i386", "--exclude=i686", ranMirror, local_dir)
	else:
		print 'false'
	

def main():
        parser = argparse.ArgumentParser(description="Python: rsyncs either CentOS or Epel repos to a local repository")
	parser.add_argument('choice',  metavar='c', type=str, help='values: C, E')
        args = parser.parse_args()
	Choice = args.choice
        _rsync(Choice)

if __name__ == '__main__':
        main()

