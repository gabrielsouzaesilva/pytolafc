import requests

import pandas as pd
import numpy as np

class Federation():
    def __init__(self) -> None:
        self._cartola_base_url = "https://api.cartolafc.globo.com/"
        self._market_status_url = self._cartola_base_url + "mercado/status"
        self._market_highlights_url = self._cartola_base_url + "mercado/destaques"
        self._rounds_url = self._cartola_base_url + "rodadas"
        self._matches_url = self._cartola_base_url + "partidas"
        self._players_url = self._cartola_base_url + "atletas/mercado"
        self._clubs_url = self._cartola_base_url + "clubes"

    def request_api_data(sefl, endpoint:str=None):
        '''
        Head function to make requests to the Cartola API

        Parameters
        ----------
        endpoint : str
            The endpoint address to make the request
        
        Returns
        -------
        Dict
            The data of the request

            Or

            Excpetion in case of response different than status code 200
        '''
        if (endpoint):
            req = requests.get(endpoint)

            if (req.status_code == 200):
                return (req.json())
            else:
                raise Exception("Something went wrong with CartolaFC Official API (x_x)")
        else:
            raise Exception("No endpoint passed ! Please provide an endpoint.")

    def get_market_status(self) -> dict:
        '''
        Get current Cartola market status

        Parameters
        ----------
        None

        Returns
        -------
        dict
            Dictionary containing the market status response
        '''
        return self.request_api_data(self._market_status_url)
        
    def get_market_highlights(self):
        '''
        Get Cartola market highlights data

        Parameters
        ----------
        param: type

        Returns
        -------
        type
            Dictionary containing the market highlights data
        '''
        return self.request_api_data(self._market_highlights_url)

    def get_rounds(self, round:int=None):
        '''
        Get Cartola round data

        Parameters
        ----------
        round: int
            The number of the round (starts from 1)

        Returns
        -------
        dict
            Dictionary containing the round data
        '''
        # Get rounds data
        rounds_data = self.request_api_data(self._rounds_url)

        if (round):
            if (round > len(rounds_data)):
                print ("Cartola only has {} ! Returning all rounds instead.".format(len(rounds_data)))
                return (rounds_data)
            elif (round < 0):
                print ("Negative round number ! Returning all rounds instead.")
                return (rounds_data)
            else:
                return (rounds_data[round-1])
        else:
            return (rounds_data)

    def get_round_matches(self, round:int=None):
        '''
        Get round matches

        Parameters
        ----------
        round : int
            The number of the round to get the matches.
            If no round number is used, returns the matches for the next round

        Returns
        -------
        dict
            Dictionary with the data for each match
        '''
        if (round):
            return self.request_api_data(self._matches_url + "/{}".format(round))
        else:
            return self.request_api_data(self._matches_url)

    def get_players(self):
        '''
        Get Cartola players

        Parameters
        ----------

        Returns
        -------
        dict
            Dictionary containing the players data
        '''
        return self.request_api_data(self._players_url)
        