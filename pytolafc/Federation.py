import requests

import pandas as pd
import numpy as np

class Federation():
    def __init__(self) -> None:
        self._market_url = "https://api.cartolafc.globo.com/mercado/"
        self._rounds_url = "https://api.cartolafc.globo.com/rodadas"
        self._matches_url = "https://api.cartolafc.globo.com/partidas"

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
        status_url = self._market_url + "status"
        req = requests.get(status_url)

        if (req.status_code == 200):
            return (req.json())
        else:
            raise Exception("Something went wrong with CartolaFC Official API (x_x)")

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
        status_url = self._market_url + "destaques"
        req = requests.get(status_url)

        if (req.status_code == 200):
            return (req.json())
        else:
            raise Exception("Something went wrong with CartolaFC Official API (x_x)")

    def get_rounds(self, round:int=None):
        '''
        Get Cartola round data

        Parameters
        ----------
        round: int
            The number of the round starting from 1

        Returns
        -------
        dict
            Dictionary containing the round data
        '''
        req = requests.get(self._rounds_url)

        if (req.status_code == 200):
            data = req.json()

            if (round > len(data)):
                print ("Cartola only has {} ! Returning all rounds instead.".format(len(data)))
                return (data)
            elif (round < 0):
                print ("Negative round number ! Returning all rounds instead.")
                return (data)
            else:
                return (data[round-1])
        else:
            print ("Status code {}".format(req.status_code))
            raise Exception("Something went wrong with CartolaFC Official API (x_x)")

    