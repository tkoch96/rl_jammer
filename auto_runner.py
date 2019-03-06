from subprocess import call, check_output
import numpy as np, json
from constants import *
min_alpha = 1.1
max_alpha = 3

for i,alpha in enumerate(np.linspace(max_alpha,min_alpha,20)):
	if i < 20:
		continue
	with open(JAM_GAME_CONFIG, 'w') as f: # change the power discrepancy factor for this simulation
		json.dump({
			"power_discrepancy_factor": alpha
		}, f)
	# call the learner
	call("python second_pass.py --mode normal --protocol ack --pkl_uid alpha_change_%d --auto_run 1 --rn 1"%i, shell=True)
	print(check_output("python create_reward_records.py --only_count 1", shell=True))