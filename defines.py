import os
from dotenv import load_dotenv
load_dotenv()

### bots ###
print(os.environ.get('MODE'))
if os.environ.get('MODE') == 'PRODUCTION':
    chores_bot = os.environ.get('BOROMIR')
    reminders_bot = os.environ.get('BOROMIR')
else:
    reminders_bot = os.environ.get('BOT_TEST')
    chores_bot = os.environ.get('BOT_TEST')

### files ###
if os.environ.get('SERVER') == 'PRODUCTION':
    fileLocation = "/home/jeb/boromir/chores2324.csv"
else:
    fileLocation = 'chores.csv'

### people in csv ###
names = {"Tim", "John", "Hank",
            "Selby", "Luke", "Jase", "William"}
