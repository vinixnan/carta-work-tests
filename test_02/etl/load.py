import pandas as pd
import numpy as np
from carta_interview import Datasets, get_data_file

class DataLoader(object):
    """Load data into postgres"""

    def load_data(self):
        patient_extract1 = get_data_file(Datasets.PATIENT_EXTRACT1)
        patient_extract2 = get_data_file(Datasets.PATIENT_EXTRACT2)
        ## Implement load into postgres