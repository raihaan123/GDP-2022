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
- Calculates the link budget of each link and optimizes various parameters


Raihaan Usman, Imperial Aeronautics GDP 2022

(Yes, I'm coding this -overkill- package because it keeps me sane...)


==================
Problem Definition
==================

[PLATFORMS]     All platforms involved in the space/ground network are registered! This includes the mothership, the drones, the GEO relays and the ground stations.

[NETWORK]       We can group several platforms into a Network() - these contain methods for selecting the best platform at a given timestep.

[LINK]          Build a graph of all the links between the platforms! The following links exist in the proposed space/ground network:

  1) Ground Network   <--->     Mothership
  2) Mothership       <--->     GEO Relay (TDRSS)
  3) Mothership       <--->     Drones (Drones are treated as a single platform)
  4) GEO Relay        <--->     Ground Network (TDRSS) - This is optional

  - Note that links have a forward and reverse direction!
  - Also note there will be times when the Ground/Mothership link is not available - TDRSS link is generally always available.
  
[ANTENNA]       Detailed antenna characteristics are defined for each platform - a platform can have multiple antennas of different types.

  - An antenna is assigned ONE link at most!
  - If multiple antennas on a platform service one link, a statemachine will determine which is utilised!
  
[STATEMACHINE]  The statemachine is used to determine which antenna is utilised for a given link given the mission state. States include:

  1) Launch                                     - Mothership/Ground:  Disabled
                                                - Mothership/TDRSS:   Enabled
                                                - Mothership/Drones:  Disabled

  2) Deploy from Falcon 9 and coast             - Mothership/Ground:  Enabled
                                                - Mothership/TDRSS:   Enabled
                                                - Mothership/Drones:  Disabled

  3) Drones Deploy                              - Mothership/Ground:  Enabled
                                                - Mothership/TDRSS:   Enabled
                                                - Mothership/Drones:  Omnidirectional antenna used

  4) Debris Observation, Detumble and Capture   - Mothership/Ground:  Enabled
                                                - Mothership/TDRSS:   Enabled
                                                - Mothership/Drones:  Directional antenna used (Horn)

  5) Deorbit                                    - Mothership/Ground:  Enabled
                                                - Mothership/TDRSS:   Enabled
                                                - Mothership/Drones:  Directional antenna used (Horn)


================================
Solving the Space/Ground Network
================================

1) Inject initial conditions for all mobile platforms - i.e the mothership! (Drones are assumed stationary relative to the mothership)

2) Run Network.select_platform(r_mothership) - this will select the best platform for the mothership to use for every network

3) Statemachine selects the desired antenna for each platform for all links

4) Calculate link budget for each link! Solve for the minimal P_tx for the mothership and drones' links for acceptable Bit Error Rate

5) Propagate the orbital position of all mobile platforms - i.e the mothership - by the timestep 'ts' and repeat from (2)!


==============
Current To-Dos
==============

- Atmosphere loss function - depends on elevation angle from ground station but can assume worst case
- Orbit propagation function - I think this is easiest to do with a library like Poliastro

Fun Plots (order of importance):
- Link diagram showing gains and losses from transmitter to receiver
- Ground station locations on a world map - with range circles for 800km altitudes
- 2D diagram of orbit of mothership and TDRSS locations

'''


from components import *
