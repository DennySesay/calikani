import requests
print("Hello clanikani")

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
        # print(data.status_code)
        print(data.json())

        return data


class AllLevelProgression:
    endpoint = '/level_progressions'

    def __init__(self, apiToken):
        self.apiToken = apiToken

    def get_progressions(self):
        data = requests.get(url=root+self.endpoint, headers=requestHeaders)
        print(data.json())
        print(data.status_code)
        return data


prog = AllLevelProgression(apiToken)
usrData = UserData(apiToken)

# prog.get_progressions()
usrData.get_user_data()
