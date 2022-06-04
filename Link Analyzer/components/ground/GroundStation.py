
class GroundStation:
    '''
    The ground station class
    '''
    
    def __init__(self, name, latitude, longitude, altitude,
                 ground_station_type, ground_station_antenna_type,
                 ground_station_antenna_gain, ground_station_antenna_height,
                 ground_station_antenna_diameter, ground_station_antenna_beamwidth,
                 ground_station_antenna_azimuth, ground_station_antenna_elevation,
                 ground_station_antenna_pattern, ground_station_antenna_pattern_type,
                 ground_station_antenna_pattern_file, ground_station_antenna_pattern_file_type,
                 ground_station_antenna_pattern_file_format, ground_station_antenna_pattern_file_resolution,
                 ground_station_antenna_pattern_file_azimuth_resolution, ground_station_antenna_pattern_file_elevation_resolution,
                 ground_station_antenna_pattern_file_azimuth_offset, ground_station_antenna_pattern_file_elevation_offset,
                 ground_station_antenna_pattern_file_azimuth_angle, ground_station_antenna_pattern_file_elevation_angle,
                 ground_station_antenna_pattern_file_azimuth_angle_resolution, ground_station_antenna_pattern_file_elevation_angle_resolution,
                 ground_station_antenna_pattern_file_azimuth_angle_offset, ground_station_antenna_pattern_file_elevation_angle_offset,
                 ground_station_antenna_pattern_file_azimuth_angle_range, ground_station_antenna_pattern_file_elevation_angle_range,
                 ground_station_antenna_pattern_file_azimuth_angle_range_resolution, ground_station_antenna_pattern_file_elevation_angle_range_resolution,
                 ground_station_antenna_pattern_file_azimuth_angle_range_offset):

        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.ground_station_type = ground_station_type
        self.ground_station_antenna_type = ground_station_antenna_type
        self.ground_station_antenna_gain = ground_station_antenna_gain
        self.ground_station_antenna_height = ground_station_antenna_height
        self.ground_station_antenna_diameter = ground_station_antenna_diameter
        self.ground_station_antenna_beamwidth = ground_station_antenna_beamwidth
        self.ground_station_antenna_azimuth = ground_station_antenna_azimuth
        self.ground_station_antenna_elevation = ground_station_antenna_elevation
        self.ground_station_antenna_pattern = ground_station_antenna_pattern
        self.ground_station_antenna_pattern_type = ground_station_antenna_pattern_type
        self.ground_station_antenna_pattern_file = ground_station_antenna_pattern_file
        self.ground_station_antenna_pattern_file_type = ground_station_antenna_pattern_file_type
        self.ground_station_antenna_pattern_file_format = ground_station_antenna_pattern_file_format
        self.ground_station_antenna_pattern_file_resolution = ground_station_antenna_pattern_file_resolution
        self.ground_station_antenna_pattern_file_azimuth_resolution = ground_station_antenna_pattern_file_azimuth_resolution
        self.ground_station_antenna_pattern_file_elevation_resolution = ground_station_antenna_pattern_file_elevation_resolution
        self.ground_station_antenna_pattern_file_azimuth_offset = ground_station_antenna_pattern_file_azimuth_offset
        self.ground_station_antenna_pattern_file_elevation_offset = ground_station_antenna_pattern_file_elevation_offset
        self.ground_station_antenna_pattern_file_azimuth_angle = ground_station_antenna_pattern_file_azimuth_angle
        self.ground_station_antenna_pattern_file_elevation_angle = ground_station_antenna_pattern_file_elevation_angle
        self.ground_station_antenna_pattern_file_azimuth_angle_resolution = ground_station_antenna_pattern_file_azimuth_angle_resolution
        self.ground_station_antenna_pattern_file_elevation_angle_resolution = ground_station_antenna_pattern_file_elevation_angle_resolution
        self.ground_station_antenna_pattern_file_azimuth_angle_offset = ground_station_antenna_pattern_file_azimuth_angle_offset
        self.ground_station_antenna_pattern_file_elevation_angle_offset = ground_station_antenna_pattern_file_elevation_angle_offset
        self.ground_station_antenna_pattern_file_azimuth_angle_range = ground_station_antenna_pattern_file_azimuth_angle_range
        self.ground_station_antenna_pattern_file_elevation_angle_range = ground_station_antenna_pattern_file_elevation_angle_range
        self.ground_station_antenna_pattern_file_azimuth_angle_range_resolution = ground_station_antenna_pattern_file_azimuth_angle_range_resolution
        self.ground_station_antenna_pattern_file_elevation_angle_range_resolution = ground_station_antenna_pattern_file_elevation_angle_range_resolution
        self.ground_station_antenna_pattern_file_azimuth_angle_range_offset = ground_station_antenna_pattern_file_azimuth_angle_range_offset
        