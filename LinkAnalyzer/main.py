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

- Atmosphere loss function - depends on elevation angle from ground station but can assume worst case
- Orbit propagation function - I think this is easiest to do with a library like Poliastro
- Network handler - Library like PyViz

Fun Plots (order of importance):
- Link diagram showing gains and losses from transmitter to receiver
- Ground station locations on a world map
- 2D diagram of orbit of mothership and TDRSS locations

'''


from components import *


# Create a list of all platforms
platforms = []

