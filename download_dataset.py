from pathlib import Path
from lerobot.datasets.lerobot_dataset import LeRobotDataset, LeRobotDatasetMetadata

ROOT_PATH = Path("./datasets/")
# REPO_ID = "a-t-i-n/record-matchbox-1"
REPO_ID = "a-t-i-n/record-test-5-charger-in-cup"
REPO_PATH_LOCAL = ROOT_PATH / REPO_ID
REPO_PATH_LOCAL.mkdir(parents=True, exist_ok=True)

ds_repo_id = REPO_ID
ds_meta = LeRobotDatasetMetadata(ds_repo_id)

print(f"Total number of episodes: {ds_meta.total_episodes}")
# print(f"Average number of frames per episode: {ds_meta.total_frames / ds_meta.total_episodes:.3f}")
# print(f"Frames per second used during data collection: {ds_meta.fps}")
# print(f"Robot type: {ds_meta.robot_type}")
# print(f"keys to access images from cameras: {ds_meta.camera_keys=}\n")

print("Tasks:")
print(ds_meta.tasks)
# print("Features:")
# pprint(ds_meta.features)

# You can also get a short summary by simply printing the object:
# print(ds_meta)

# You can then load the actual dataset from the hub.
# Either load any subset of episodes:
dataset = LeRobotDataset(ds_repo_id, root=REPO_PATH_LOCAL)
