import math

def reward_function(params):
	'''
	Example of rewarding the agent to stay inside the two borders of the track
	'''

	# Read input parameters
	all_wheels_on_track = params['all_wheels_on_track']
	distance_from_center = params['distance_from_center']
	track_width = params['track_width']
	steering = abs(params['steering_angle'])
	direction_stearing=params['steering_angle']
	speed = params['speed']
	steps = params['steps']
	progress = params['progress']
	all_wheels_on_track = params['all_wheels_on_track']

	ABS_STEERING_THRESHOLD = 15
	SPEED_TRESHOLD = 5
	TOTAL_NUM_STEPS = 85

	waypoints = params['waypoints']
	closest_waypoints = params['closest_waypoints']
	heading = params['heading']

	# Give a very low reward by default
	reward = 1.0

	if progress == 100:
		reward += 100

	 # Calculate the direction of the center line based on the closest waypoints
	next_point = waypoints[closest_waypoints[1]]
	prev_point = waypoints[closest_waypoints[0]]

	# Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
	track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])

	# Convert to degree
	track_direction = math.degrees(track_direction)

	# Calculate the difference between the track direction and the heading direction of the car
	direction_diff = abs(track_direction - heading)

	# Penalize the reward if the difference is too large
	DIRECTION_THRESHOLD = 10.0
	malus=1

	# Give a high reward if no wheels go off the track and
	# the agent is somewhere in between the track borders
	if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
		reward = 1.0

	if direction_diff > DIRECTION_THRESHOLD:
		malus=1-(direction_diff/50)

	if malus<0 or malus>1:
		malus = 0
		reward *= malus

	# Always return a float value
	return float(reward)
