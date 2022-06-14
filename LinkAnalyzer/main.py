''' 
  _     _       _         _                _                    
 | |   (_)_ __ | | __    / \   _ __   __ _| |_   _ _______ _ __ 
 | |   | | '_ \| |/ /   / _ \ | '_ \ / _` | | | | |_  / _ \ '__|
 | |___| | | | |   <   / ___ \| | | | (_| | | |_| |/ /  __/ |   
 |_____|_|_| |_|_|\_\ /_/   \_\_| |_|\__,_|_|\__, /___\___|_|   
                                             |___/             

The Ultimate Link Budget tool!

- Builds a graph of all links between the nodes in the space/ground network
- Integrates requirements and constraints of the overall spacecraft system
- Calculates the link budget of each link


Raihaan Usman, Imperial Aeronautics GDP 2022

(Yes, I'm coding this -overkill- library because it keeps me sane...)


------------
How it works
------------

The following links exist in the proposed space/ground network:

Ground        <--->   Mothership
Mothership    <--->   GEO Relay (TDRSS)
GEO Relay     <--->   Ground (TDRSS)

Note that links have a forward and reverse direction.

Also note there will be times when the Ground/Mothership link is not available - TDRSS link is generally always available.


- After propagating orbital position of the mothership/drones, the nearest TDRSS link is identified for each position.
- The contact time for the faster Direct to Ground (DTE) link is calculated for each position.
    - It is intended for exchanging less critical data at higher rates, including live video and point-clouds.


--------------
Current To-Dos
--------------

- Atmosphere loss function - depends on elevation angle from ground station but can assume wosrst case
- Orbit propagation function - I think this is easiest to do with a library like 
- Network handler

'''


from LinkAnalyzer.components import *


platforms = []

# Create a list of all platforms

