import slack
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime

def read_json_files(file_name):
    # create new json files
    file = open(file_name, "r")
    return json.load(file)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

today_date = datetime.today().strftime('%Y-%m-%d')

holidays_file = read_json_files('list_of_holidays_per_date.json')
text_to_print = []
if (holidays_file[str(today_date)]):
    num_of_holidays = len(holidays_file[str(today_date)])
    holiday_word = 'holiday' if num_of_holidays == 1 else 'holidays'

    text_to_print.append(f'Today, the world celebrates {num_of_holidays} {holiday_word} \n')
    count = 1
    for holidays in holidays_file[str(today_date)]:
        holiday_name = holidays['holiday_name']
        country_name = holidays['country_name']
        text_to_print.append(f'{count}. Holiday: {holiday_name} | Country: {country_name} \n')
        count += 1

client.chat_postMessage(channel='#holiday-reminder', text=" ".join(text_to_print)    )
