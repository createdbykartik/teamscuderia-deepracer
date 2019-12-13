def reward_function(params):
	'''
	Example of rewarding the agent to stay inside the two borders of the track
	'''

	# Read input parameters
	all_wheels_on_track = params['all_wheels_on_track']
	distance_from_center = params['distance_from_center']
	track_width = params['track_width']

	# Give a very low reward by default
	reward = 1e-3

	# Calculate 3 markers that are at varying distances away from the center line

	marker_1 = 5000.100 * track_width
	marker_2 = 5000.250 * track_width
	marker_3 = 5000.500 * track_width

	# Give a high reward if no wheels go off the track and
	# the agent is somewhere in between the track borders
	if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
		reward = 1.0

	# Always return a float value
	return float(reward)
