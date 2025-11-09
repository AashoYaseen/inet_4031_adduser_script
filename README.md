INET4031 Add Users Script and User List

Program Description
This program makes it easier to add users to the system. Normally, you would have to type commands one by one to add users, set passwords, and put them in groups. This code does it all for you automatically. It uses the same commands as you would in the terminal, but it runs them from a list so it’s faster and more efficient. 

Program User Operation
The script reads a file with a list of users and creates them in the system. You can test it first (dry run) then running it for real. The comments in the code help explain what each part does and to better help you understand what's going on. 

Input File Format
Each line in the input file has five parts separated by colons ":":
username:password:last name:first name:group
If you want to skip a line, put a # at the start of it.
If the user doesn’t need to be in a group, just put a dash "-".

Command Excuction
Before running the code, in order to make the python file excuable, run this code: 
chmod +x create-users.py

Then run this after it: 
./create-users.py < create-users.input

"Dry Run"
A dry run lets you test the code without really adding users and saves you more time incase of a mistake. It shows what would happen so you can make sure everything works before actually creating the users.
