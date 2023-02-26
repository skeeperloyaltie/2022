# Goal:

# Think of this task as a vocabulary matching problem where you match terms of the same meaning. We have two different sources reporting data; 
# source 1 and source 2. The two sources use different methods of assigning names to the commodity terms. We would like you to align these two 
# different data sources;  whenever the same agricultural commodity appears in both sources, match them and represent them as a pair.


# The two sources are of different sizes; and thus not all terms have corresponding pairs. You may notice that some terms in source 1 are not 
# expressed in perfect English

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import mpl_toolkits
# import the datasets
source_1 = pd.read_csv('source_1.csv')
source_2 = pd.read_csv('source_2.csv')

# merge the two datasets
source_1['name'] = 'name_1'
source_2['name'] = 'name_2'

# merge the two datasets
source_1['name'] = 'name_1'
source_2['name'] = 'name_2'
