import requests
import json
import argparse

# dont publish to aur until removal of test token
apiToken = 'afefc447-fa06-46f7-9bd0-f60c81049a5f'
revision = 20170710
root = 'https://api.wanikani.com/v2'
requestHeaders = {
    'Wanikani-Revision': f'{revision}',
    'Authorization': 'Bearer ' + f'{apiToken}'
}


class UserData:
    endpoint = '/user'

    def __init__(self, apiToken):
        self.apiToken = apiToken

    def get_user_data(self):
        data = requests.get(url=root+self.endpoint, headers=requestHeaders)
        userdata = json.dumps(data.json(), indent=4)
        print(data.status_code)
        print(userdata)
        # print(data.json())

        return userdata


class Summary:
    endpoint = '/summary'

    def __init__(self, apiToken):
        self.apiToken = apiToken

    def get_summary(self):
        data = requests.get(url=root+self.endpoint, headers=requestHeaders)
        summary = json.dumps(data.json(), indent=4)
        print(data.status_code)
        print(summary)

        return summary


class AllLevelProgression:
    endpoint = '/level_progressions'

    def __init__(self, apiToken):
        self.apiToken = apiToken

    def get_progressions(self):
        data = requests.get(url=root+self.endpoint, headers=requestHeaders)
        progressions = json.dumps(data.json(), indent=4)
        print(data.status_code)
        print(progressions)

        return progressions


parser = argparse.ArgumentParser()
parser.add_argument("--userdata", help="retrieves userdata", action="store_true")
parser.add_argument("--summary", help="retrieves current and upcomming reviews", action="store_true")
parser.add_argument("--levelprogressions", help="retrieves levelprogressions" ,action="store_true")
args = parser.parse_args()

if args.userdata:
    usrData = UserData(apiToken)
    usrData.get_user_data()
elif args.levelprogressions:
    prog = AllLevelProgression(apiToken)
    prog.get_progressions()
elif args.summary:
    summary = Summary(apiToken)
    summary.get_summary()
