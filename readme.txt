Step - 1
#Clone the Repository by command :
git clone git@github.com:Avinash-Ch-11/Flask_cal.git

/-----------------------------------------------------------------------------------------------------

Step - 2
#In terminal type the command: "cd Flask_cal/"

/-----------------------------------------------------------------------------------------------------

Step - 3
#In terminal type the command: "python3 -m venv venv"

/-----------------------------------------------------------------------------------------------------

Step - 4
#In terminal type the command: "source venv/bin/activate"

/-----------------------------------------------------------------------------------------------------

Step - 5
#In terminal type the command: "pip install -r Requirements.txt"

/-----------------------------------------------------------------------------------------------------

After all the requirements had downloaded,
Step - 6
#In terminal type the command: "sqlite3 db.sqlite3"          #db.sqlite3 is my database name

/-----------------------------------------------------------------------------------------------------

Step - 7
#In terminal type the command: ".databases"

/-----------------------------------------------------------------------------------------------------

Step - 8
#In terminal type the command: ".quit"

/-----------------------------------------------------------------------------------------------------

Step - 9
After quitting from the sqlite3,type the below command in the terminal:
python3 create_table.py

/-----------------------------------------------------------------------------------------------------

Step - 10
I think the given, requirements are satisfied according to my views. So, let's start the given problem:
In terminal type the command: "python3 app.py"
After this command the server starts.

/-----------------------------------------------------------------------------------------------------

Step - 11
Go to the localhost in the google chrome ( or ) click on the link which is displayed on the terminal:
My localhost url or ip address : http://127.0.0.1:5000/
Result : "Hi from test API"

/-----------------------------------------------------------------------------------------------------

Step - 12
My localhost url or ip address : http://127.0.0.1:5000/calculate/num1/num2
Example : http://127.0.0.1:5000/calculate/2/8
From the above example the result is displayed i.e unique_identifier on the chrome
unique_identifier = id = '7582d5eb-9e40-455e-985b-ef2b1a0130e6'

/-----------------------------------------------------------------------------------------------------

Step - 13
For /get_answer/identifier/ to view this result:
In the url type the following command : http://127.0.0.1:5000/get_answer/identifier
identifier = unique_identifier = id
For example : http://127.0.0.1:5000/get_answer/7582d5eb-9e40-455e-985b-ef2b1a0130e6
0cc038b8-3046-4b6f-b284-68f55d34fffc --- This is the identifier

After the command it takes some seconds to calculate the answer and it displays the some message on the screen i.e "please wait"

After this message displayed on the screen, please reload the page to display the answer i.e "10"

/-----------------------------------------------------------------------------------------------------

Step - 14
If you want to the see the data which u have entered in the url i.e database
Please type the following command to see the database: "sqlite3 db.sqlite3"
After the above command type the next command: "select * from user"
Next, the command: ";" then hit enter.
Then, the data which u have stored in the database will be displayed on the terminal. 

For example:
9f9096d5-aba1-4bd2-8955-62ac5edaf104|12|12|24
id = 9f9096d5-aba1-4bd2-8955-62ac5edaf104
num1 = 12
num2 = 12
sum = 24

/-----------------------------------------------------------------------------------------------------

Finally,this is my project which is assigned to me.
If you find any errors or any kind of problem please let me know. I'm adding my email at the last.
Thanking You

Yours sincerely
CHILAKA AVINASH
Roll no.: 180010011
Email Id: 180010011@iitdh.ac.in










