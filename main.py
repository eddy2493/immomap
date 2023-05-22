# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:50:12 2023

@author: gnms
"""

import immoscoutAPI
import homegateAPI

homegateResults = homegateAPI.get_listings(2504, 'BUY')
immoscoutResults = immoscoutAPI.get_listings(2504, 'BUY')