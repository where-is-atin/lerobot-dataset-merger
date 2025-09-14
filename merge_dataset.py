# %%
from lerobot.datasets.lerobot_dataset import LeRobotDataset, LeRobotDatasetMetadata
from pathlib import Path
from dataclasses import dataclass


# %%
ds_root = Path('./datasets/')
ds1_repo_id = 'a-t-i-n/record-matchbox-1'
ds1_local_path = ds_root / ds1_repo_id
assert ds1_local_path.is_dir()

ds2_repo_id = 'a-t-i-n/record-test-5-charger-in-cup'
ds2_local_path = ds_root / ds2_repo_id
assert ds2_local_path.is_dir()


# - data, - meta, -videos and
# merge data
