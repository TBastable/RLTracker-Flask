import requests


class PlayerStats:
    def __init__(self,
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

    @staticmethod
    def generate_response(username, platform):
        url = f'https://api.tracker.gg/api/v2/rocket-league/standard/profile/{platform}/{username}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if not response.ok:
            print(f"API failed with a {response.status_code} response - aborting")
            return
        raw_response_data = response.json().get("data", {})
        return raw_response_data

    def extract_player_stats_from_response(self, raw_response_data):
        platform_dic = {'xbl': 'Xbox Live', 'psn': 'Playstation Network', 'steam': 'Steam'}
        self.platform = platform_dic[raw_response_data['platformInfo']['platformSlug']]
        self.username = raw_response_data
        self.username = raw_response_data['platformInfo']['platformUserHandle']
        self.season_name = raw_response_data['metadata']['currentSeason']
        self.lifetime_wins = raw_response_data['segments'][0]['stats']['wins']['displayValue']
        self.mvps = raw_response_data['segments'][0]['stats']['mVPs']['displayValue']
        self.goals = raw_response_data['segments'][0]['stats']['goals']['displayValue']
        self.saves = raw_response_data['segments'][0]['stats']['saves']['displayValue']
        self.shots = raw_response_data['segments'][0]['stats']['shots']['displayValue']
        self.assists = raw_response_data['segments'][0]['stats']['assists']['displayValue']
        self.lifetime_win_rank = raw_response_data['segments'][0]['stats']['wins']['rank']
        self.goal_shot_ratio = raw_response_data['segments'][0]['stats']['goalShotRatio']['displayValue']
        self.season_reward = raw_response_data['segments'][0]['stats']['seasonRewardLevel']['metadata'][
            'rankName']
        match_dic = {}
        for i in range(2, 10):
            match = raw_response_data['segments'][i]['stats']['matchesPlayed']['value']
            name = raw_response_data['segments'][i]['metadata']['name']
            rank = raw_response_data['segments'][i]['metadata']['name']
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