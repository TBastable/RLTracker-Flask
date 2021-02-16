import requests


class PlayerStats:
    def __init__(self,
                 raw_response_data,
                 platform=None,
                 username=None,
                 season_name=None,
                 lifetime_wins=None,
                 lifetime_win_rank=None,
                 mvps=None,
                 goal_shot_ratio=None,
                 season_reward=None,
                 game_data=None,
                 match_info=None,
                 goals=None,
                 saves=None,
                 shots=None,
                 assists=None
                 ):
        self.platform = platform
        self.username = username
        self.season_name = season_name
        self.lifetime_wins = lifetime_wins
        self.lifetime_win_rank = lifetime_win_rank
        self.goal_shot_ratio = goal_shot_ratio
        self.season_reward = season_reward
        self.game_data = game_data
        self.match_info = match_info
        self.mvps = mvps
        self.goals = goals
        self.saves = saves
        self.shots = shots
        self.assists = assists
        self.raw_response_data = raw_response_data
        self.extract_player_stats_from_response()

    def extract_player_stats_from_response(self):
        platform_dic = {'xbl': 'Xbox Live', 'psn': 'Playstation Network', 'steam': 'Steam'}
        self.platform = platform_dic[self.raw_response_data['platformInfo']['platformSlug']]
        self.username = self.raw_response_data['platformInfo']['platformUserHandle']
        self.season_name = self.raw_response_data['metadata']['currentSeason']
        self.lifetime_wins = self.raw_response_data['segments'][0]['stats']['wins']['displayValue']
        self.mvps = self.raw_response_data['segments'][0]['stats']['mVPs']['displayValue']
        self.goals = self.raw_response_data['segments'][0]['stats']['goals']['displayValue']
        self.saves = self.raw_response_data['segments'][0]['stats']['saves']['displayValue']
        self.shots = self.raw_response_data['segments'][0]['stats']['shots']['displayValue']
        self.assists = self.raw_response_data['segments'][0]['stats']['assists']['displayValue']
        self.lifetime_win_rank = self.raw_response_data['segments'][0]['stats']['wins']['rank']
        self.goal_shot_ratio = self.raw_response_data['segments'][0]['stats']['goalShotRatio']['displayValue']
        self.season_reward = self.raw_response_data['segments'][0]['stats']['seasonRewardLevel']['metadata'][
            'rankName']
        match_dic = {}
        for i in range(2, 10):
            match = self.raw_response_data['segments'][i]['stats']['matchesPlayed']['value']
            name = self.raw_response_data['segments'][i]['metadata']['name']
            rank = self.raw_response_data['segments'][i]['metadata']['name']
            match_dic[name] = (match, rank)
        self.match_info = match_dic
        return

    def tracker_data_print(self):
        """A simple function for printing results of custom dictionary passed to it"""
        print(f"These are the Rocket League user stats for {self.username}, playing on {self.platform}\n"
              f"We are currently playing in Season {self.season_name}, "
              f"and you will be receiving {self.season_reward} season rewards\n"
              f"Lifetime stats\n"
              f"Lifetime wins: {self.lifetime_wins}\n"
              f"Lifetime win rank: {self.lifetime_win_rank}\n"
              f"Lifetime goal to shot ratio: {self.goal_shot_ratio}%")


class TrackerAPI:
    def __init__(self, platform, username):
        self.platform = platform
        self.user = str.replace(username, " ", "%20")
        self.raw_response_data = None
        self.response = None
        self.get_response()

    def get_response(self):
        url = f'https://api.tracker.gg/api/v2/rocket-league/standard/profile/{self.platform}/{self.user}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if not response.ok:
            self.response = False
        else:
            self.response = True
        raw_response_data = response.json().get("data", {})
        self.raw_response_data = raw_response_data
        return



response = TrackerAPI('xbl', "UKF WONDERBOY2")

print(response.response)

if not response.response:
    print(f'Error receiving data for {response.user}. Please check spelling and platform and try again.')