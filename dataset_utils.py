from lerobot.datasets.lerobot_dataset import LeRobotDataset, LeRobotDatasetMetadata
from pathlib import Path

ROOT_DIR = Path('./datasets')


def load_dataset(repo_id: str) -> LeRobotDataset:
    ds_local_path = ROOT_DIR / repo_id
    return LeRobotDataset(root=ds_local_path, repo_id=repo_id)
