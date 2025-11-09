#!/usr/bin/python3

# INET4031
# Aasho Yaseen
# Date Created: 2025-11-09
# Date Last Modified: 2025-11-09

#Import os runs the system, import re does the matching patterns and sys reads the files
import os
import re
import sys

def main():
    for line in sys.stdin:

        #looks for lines that start with # to skip them 
        match = re.match("^#",line)

        #splits each line with ":" and removes spaces
        fields = line.strip().split(':')

        #Skips the liens that dont have 5 fields 
        if match or len(fields) != 5:
            continue

        #has the username, password, last name and first name to help match for when searched for 
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #This is the group line which is in field 4 for outputs and splits using "," incase of more groups per user
        groups = fields[4].split(',')

        #shows what user account is being created
        print("==> Creating account for %s..." % (username))
        #the command to add the user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
        
        #print cmd
        #os.system(cmd)

        #asking for the set password for the user
        print("==> Setting the password for %s..." % (username))
        # the commad that asks for password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd
        #os.system(cmd)

        for group in groups:
            #checks if there’s a group listed; if yes, adds the user to it
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
