# Example for numObsInSurveyTimeOverlap
# Somayeh Khakpash - Lehigh University
# Last edited : 11/20/2018
# Calculates number of observations during simultaneous windows of another survey.
# SurveyObsWin is the list of the survey observing window/inter-seasonal gap intervals. It should be in the format:
# SurveyObsWin = [ [YYYY-MM-DD, YYYY-MM-DD] , [YYYY-MM-DD, YYYY-MM-DD] , ... , [YYYY-MM-DD, YYYY-MM-DD] ]

import numpy as np 
from astropy.time import Time
from lsst.sims.maf.metrics import BaseMetric

class numObsInSurveyTimeOverlap (BaseMetric):
    
    
    def __init__ (self, SurveyObsWin, TimeCol='observationStartMJD',metricName= 'numObsInSurveyTimeOverlap', **kwargs):
        
        self.TimeCol = TimeCol
        self.metricName = metricName
        self.SurveyObsWin = SurveyObsWin
        super(numObsInSurveyTimeOverlap, self).__init__(col= TimeCol, metricName=metricName, **kwargs)
        
    def run (self, dataSlice, slicePoint=None):
        N_Obs = 0
        for interval in self.SurveyObsWin :
            start_interval = Time(interval[0]+' 00:00:00')
            end_interval = Time(interval[1]+' 00:00:00')
            index = np.where ((dataSlice[self.TimeCol]> start_interval.mjd) & (dataSlice[self.TimeCol]<end_interval.mjd))[0]
            N_Obs = N_Obs + np.size(index)
        
        return N_Obs
