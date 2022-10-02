
import botometer

class Botmeter:
    def __init__(self, keys):
        twitter_app_auth = {
            'consumer_key': keys["API_KEY"],
            'consumer_secret': keys["API_SECRET"],
            'access_token': keys["ACCESS_TOKEN"],
            'access_token_secret': keys["ACCESS_TOKEN_SECRET"],
        }
        self.botDetector = botometer.Botometer(wait_on_ratelimit=True,
                                               rapidapi_key=keys["RAPIDAPI"],
                                               **twitter_app_auth)
    def checkAccount(self, account):
        return self.botDetector.check_account(account)
    def checkAccountList(self, accountList):
        return self.botDetector.check_accounts_in(accountList)