from crontab import CronTab

'''
    pip install python-crontab
'''

user = "INSERT_USER"
command = "python3 /home/USER/DIRECTORY/tiktok_ig.py"

# It works for Linux systems
cron = CronTab(user=user)
job = cron.new(command=command)
job.setall('0 4 * * *') # Every day at 04:00
cron.write()