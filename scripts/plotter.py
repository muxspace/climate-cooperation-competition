import os
from glob import glob
from opt_helper import get_training_curve, plot_training_curve, plot_results
from desired_outputs import desired_outputs


_ROOT = os.getcwd()

def outputs(metric='global_temperature'):
  """
  desired_outputs = ['global_temperature',
  'global_carbon_mass',
  'capital_all_regions',
  'labor_all_regions',
  'production_factor_all_regions',
  'intensity_all_regions',
  'global_exogenous_emissions',
  'global_land_emissions',
  'timestep',
  'activity_timestep',
  'capital_depreciation_all_regions',
  'savings_all_regions',
  'mitigation_rate_all_regions',
  'max_export_limit_all_regions',
  'mitigation_cost_all_regions',
  'damages_all_regions',
  'abatement_cost_all_regions',
  'utility_all_regions',
  'social_welfare_all_regions',
  'reward_all_regions',
  'consumption_all_regions',
  'current_balance_all_regions',
  'gross_output_all_regions',
  'investment_all_regions',
  'production_all_regions',
  'tariffs',
  'future_tariffs',
  'scaled_imports',
  'desired_imports',
  'tariffed_imports',
  'stage',
  'minimum_mitigation_rate_all_regions',
  'promised_mitigation_rate',
  'requested_mitigation_rate',
  'proposal_decisions',
  'global_consumption',
  'global_production']
  """
  plot_result(metric,
  nego_off=gpu_nego_off_ts, # change it to cpu_nego_off_ts if using CPU
  nego_on=gpu_nego_on_ts,
  k=0)



def training_curve(metric='Mean episodic reward', index=0):
  """
  These are all available via Tensorboard.

  metrics = ['Iterations Completed',
   'VF loss coefficient',
   'Entropy coefficient',
   'Total loss',
   'Policy loss',
   'Value function loss',
   'Mean rewards',
   'Max. rewards',
   'Min. rewards',
   'Mean value function',
   'Mean advantages',
   'Mean (norm.) advantages',
   'Mean (discounted) returns',
   'Mean normalized returns',
   'Mean entropy',
   'Variance explained by the value function',
   'Gradient norm',
   'Learning rate',
   'Mean episodic reward',
   'Mean policy eval time per iter (ms)',
   'Mean action sample time per iter (ms)',
   'Mean env. step time per iter (ms)',
   'Mean training time per iter (ms)',
   'Mean total time per iter (ms)',
   'Mean steps per sec (policy eval)',
   'Mean steps per sec (action sample)',
   'Mean steps per sec (env. step)',
   'Mean steps per sec (training time)',
   'Mean steps per sec (total)'
   ]
  """
  glob(os.path.join(_ROOT,"Submissions/*.zip"))
  log_zip = os.path.basename(glob(os.path.join(_ROOT,"Submissions/*.zip"))[index]) 
  plot_training_curve(None, metric, log_zip)


