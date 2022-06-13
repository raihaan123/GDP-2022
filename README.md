# GDP-2022
Repository for project work for the space debris removal GDP at Imperial Aeronautics

## Link Analyzer
A python package to dynamically compute all link budgets in **any** space/ground network!

1. Define all networked platforms involved in the mission - ```GroundStation()```, ```Satellite()```, and ```GEORelay()``` extend ```Platform()```
    - Propagate satellite positions for the duration of the mission
</br>
2. Set antenna configurations mounted on each platform - ```ShapedAntenna()``` and ```PhasedArray()``` extend the general ```Antenna()```
</br>
3. Define all links between platforms - ```RF()``` and ```Optical()``` extend ```Link()```
</br>
4. Compute all link margins
</br>
5. Calculate optimal parameters for each link through iterative optimisation