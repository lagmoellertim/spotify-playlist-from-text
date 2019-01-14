import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyText:
    def __init__(self, client_id, client_secret, verbose=False):
        self.client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.spotipy_object = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        self.verbose = verbose

    def __song_available(self, string):
        result = self.spotipy_object.search(q=string, limit=50)
        for name, uri in [(x['name'], x["uri"]) for x in result['tracks']['items']]:
            filtered = self.__filter_string(name)
            if filtered == string:
                return name, uri

    @staticmethod
    def __filter_string(string):
        filtered = re.sub(' +', ' ', ''.join(x for x in string if x.isalpha() or x == " ").lower())
        if len(filtered) > 0:
            return filtered[1:] if filtered[0] == " " else filtered
        else:
            return ""

    @staticmethod
    def __generate_string_combinations(string, max_title_length=3):
        string_list = string.split(" ")
        combinations = []
        for i, x in enumerate(string_list):
            for title_length in range(1, max_title_length + 1):
                if len(string_list) >= i + title_length:
                    combinations.append(" ".join(string_list[i:i + title_length]))
        return combinations

    def __generate_word_tree(self, string_combinations, filtered_text):
        word_tree = {}
        for string in string_combinations:
            song = self.__song_available(string)
            if song is not None:
                indices = [m.start() for m in re.finditer(string, filtered_text)]
                for index in indices:
                    if index not in word_tree.keys():
                        word_tree[index] = []
                    item = [song[0], song[1], index + len(string) + 1]
                    if item not in word_tree[index]:
                        word_tree[index].append(item)
                        if self.verbose:
                            print(item)
        return word_tree

    def __recursive_tree_check(self, start_num, word_tree, filtered_text):
        if start_num == len(filtered_text) + 1:
            return True

        results = []
        if start_num in word_tree.keys():
            for i, x in enumerate(word_tree[start_num]):
                results.append([i, self.__recursive_tree_check(x[2], word_tree, filtered_text)])
        for item in results:
            if item[1] is True:
                return [[start_num, item[0]]]
            elif item[1] is not False:
                return [[start_num, item[0]], (*item[1])]
        else:
            return False

    def generate_playlist(self, text, max_title_length=3):
        filtered_text = self.__filter_string(text)
        combinations = self.__generate_string_combinations(filtered_text,
                                                           max_title_length=max_title_length)
        word_tree = self.__generate_word_tree(combinations, filtered_text)
        correct_path = self.__recursive_tree_check(0, word_tree, filtered_text)

        return [word_tree[x][y][:2] for x, y in correct_path] if correct_path else False