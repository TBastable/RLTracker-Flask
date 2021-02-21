import requests


class PlayerStats:
    """
        Class to store user statistics based on dictionary file of raw data
    """

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
        """
        Initialises creation of all class properties for stats storage.
        :param raw_response_data: JSON/Dictionary type generated from Tracker.gg API response
        :param: All other parameters initialised, but generated within a class method
        """
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

    def extract_player_stats_from_response(self) -> None:
        """
        From JSON data takes key information on players' stats and stores them as class properties.
        :return: None
        """
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


class TrackerAPI:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Safari/537.36'}

    @classmethod
    def get_user_profile_data(cls, platform, user_id):
        """
        Generates a JSON/Dictionary response from tracker.gg API endpoint. Checks for errors within the API response.
        :return: Stores a dictionary of raw response data and any API response errors
        """
        user_id_no_space = str.replace(user_id, " ", "%20")
        url = f'https://api.tracker.gg/api/v2/rocket-league/standard/profile/{platform}/{user_id_no_space}'
        response = requests.get(url, headers=cls.headers)
        response.raise_for_status()
        return response.json().get("data", {})
