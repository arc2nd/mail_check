1) edit the 'envs.json' file for your email account
2) run 'python make_crypt.py'. This should create a file 'envs.crypt'
3) delete 'envs.json'
4) go through 'mail_check.py' and make sure all the absolute paths 
    are ok
5) curate the python files in the commands folder, the function name 
    and the file name must match. If you are not using my pellets 
    repo you should get rid of msg.py

Every time the script runs, it should decrypt the 'envs.crypt' file
and put them into the python process's environment variables. The 
script will then query the environment variables for addresses and 
passwords.

Example cron:
/5 * * * * /usr/bin/python /home/pi/scripts/mail_check/mail_check.py > /home/pi/crontab_output.txt

You can now send yourself emails where the subject is "CMD: <arbitrary 
text> and the body is something like: `<cmd>%<arguments>`

If you are using my pellets repo with RabbitMQ you can send a email 
with the body being something like:
`msg%<cmd><first arg>[,<second arg>,<third args>,...]`

Update 11-30-18:

mail_check.py is run as a cron job

+ it checks the email and executes the plugin commands
+ if the msg plugin is called it will generate a RabbitMQ message

MailReceiver.py is run as a service

+ it relies on my pellets repo to build RabbitMQ consumers
+ when a message comes in it calls a mail_check plugin
+ accepts messages from anywhere, not just mail_check
