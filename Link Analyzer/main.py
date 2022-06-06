''' 
Link Analyzer - The Ultimate Link Budget tool!

- Builds a graph of all links between the nodes in the space/ground network
- Integrates requirements and constraints of the overall spacecraft system
- Calculates the link budget of each link


Raihaan Usman, Imperial Aeronautics GDP 2022

(Yes, I'm coding this -overkill- library because it keeps me sane...)
'''

import numpy as np

# Importing ground segment classes
from components import GroundStation as gs
from components import MissionControl as mc
from components import EndUser as eu

# Importing space segment classes
from components import Mothership as ms

# Importing link classes
from components import RF



# TODO:
# Add ground traces from the mothership/drones - use Poliastro
