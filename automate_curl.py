import random
import requests
from datetime import datetime

# Get current date in the required format
current_date = datetime.now().strftime("%d-%b-%Y")

# Arrays for random data
random_task_array = [
    "Bug fixing in Deprovisioning task",
    "Code optimization",
    "Feature development",
    "Writing test cases for deprovisioning task",
    "Documentation of Deprovisioning API",
    "Refactoring",
    "Research and development",
    "Implementation of the Mimic app"
]

random_wins_array = [
    "Completed tasks on time",
    "Resolved a critical bug",
    "Achieved a project milestone",
    "Optimized the codebase",
    "Implemented a new feature",
    "-"
]

meeting_highlight_array = [
    "Confidential",
    "Regular daily standup"
]

# Randomly select data
task = random.choice(random_task_array)
win = random.choice(random_wins_array)
meeting_highlight = random.choice(meeting_highlight_array)

# Prepare the payload
payload = {
    "Email": "tanishq.patidar@kalvium.community",
    "Date": current_date,  # Use current date
    "TermsConditions": "true",
    "Dropdown": "Work Integrated - Industry",
    "Dropdown1": "Josys",
    "MultiLine": task,
    "Slider": "5",
    "MultiLine1": win,
    "Slider2": "5",
    "MultiLine5": win,
    "Radio": "Yes",
    "MultiLine6": meeting_highlight,
    "REFERRER_NAME": "https://forms.zohopublic.in/gurmindersinghkal1/form/Signup/thankyou/formperma/GeJFMLBDfoWlIJfhI46Qyx0Dlf3kHhMSRsvMItq_Riw"
}

# Headers for the request
headers = {
    "Accept": "application/zoho.forms-v1+json",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": "zalb_fb90f7f307=aac3771a758cfd755b2a8a0b2e4ba31e",
    "DNT": "1",
    "Origin": "https://forms.zohopublic.in",
    "Referer": "https://forms.zohopublic.in/gurmindersinghkal1/form/Signup/formperma/GeJFMLBDfoWlIJfhI46Qyx0Dlf3kHhMSRsvMItq_Riw",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"'
}

# Make the request
try:
    response = requests.post(
        "https://forms.zohopublic.in/gurmindersinghkal1/form/Signup/formperma/GeJFMLBDfoWlIJfhI46Qyx0Dlf3kHhMSRsvMItq_Riw/records",
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    print("Request successful!")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    # Exit with error to trigger failure notification
    exit(1)