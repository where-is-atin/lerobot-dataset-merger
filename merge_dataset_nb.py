import marimo

__generated_with = "0.15.3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    from lerobot.datasets.lerobot_dataset import (
        LeRobotDataset,
        LeRobotDatasetMetadata,
    )
    from pathlib import Path
    from dataclasses import dataclass
    return Path, mo


@app.cell
def _(Path):
    ds_root = Path("./datasets/")
    ds1_repo_id = "a-t-i-n/record-matchbox-1"
    ds1_local_path = ds_root / ds1_repo_id
    assert ds1_local_path.is_dir()

    ds2_repo_id = "a-t-i-n/record-test-5-charger-in-cup"
    ds2_local_path = ds_root / ds2_repo_id
    assert ds2_local_path.is_dir()

    # - data, - meta, -videos and
    # merge data
    return ds1_local_path, ds2_local_path, ds_root


@app.cell
def _(ds_root):
    # create folder
    dsm_repo_id = "merged/merged-ds"
    dsm_local_path = ds_root / dsm_repo_id
    import shutil, os, sys

    if dsm_local_path.is_dir():
        print("looks to be a dir, cleaning")
        shutil.rmtree(dsm_local_path)

    dsm_local_path.mkdir(parents=True, exist_ok=True)
    dsm_data_dir = dsm_local_path / "data"
    dsm_meta_dir = dsm_local_path / "meta"
    dsm_meta_dir.mkdir()
    dsm_videos_dir = dsm_local_path / "videos"
    dsm_videos_dir.mkdir()
    return (dsm_data_dir,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ### DATA

    - `chunk-000` # chunks_size decided by info.json, default 1000 episodes
        - `episode_00000n.parquet`
            - action, observation.state,  
    """
    )
    return


@app.cell
def _(ds1_local_path):
    import polars as pl

    ds1e1_path = ds1_local_path / "data/chunk-000/episode_000001.parquet"
    ds1e1 = pl.read_parquet(ds1e1_path)
    ds1e1
    return ds1e1, pl


@app.cell
def _(ds1e1):
    ds1e1.collect_schema()
    return


@app.cell
def _(ds1e1):
    print(ds1e1.head())
    return


@app.cell
def _(ds1_local_path, ds2_local_path, dsm_data_dir):
    ds1_chunk_dir = ds1_local_path / "data/chunk-000"
    ds2_chunk_dir = ds2_local_path / "data/chunk-000"
    dsm_chunk_dir = dsm_data_dir / "chunk-000"
    dsm_chunk_dir.mkdir(parents=True, exist_ok=True)
    return ds1_chunk_dir, ds2_chunk_dir, dsm_chunk_dir


@app.cell
def _(ds1_chunk_dir, ds2_chunk_dir):
    eps_to_merge = sorted(ds1_chunk_dir.glob("*.parquet")) + sorted(
        ds2_chunk_dir.glob("*.parquet")
    )
    eps_to_merge
    return (eps_to_merge,)


@app.cell
def _(dsm_chunk_dir, eps_to_merge, pl):
    ep_ix_new = 0
    frame_counter = 0
    print(f"Found {len(eps_to_merge)} episodes to merge")
    for ep_fp in eps_to_merge:
        ep = pl.read_parquet(ep_fp)
        ep_reix = ep.with_columns(
            pl.lit(ep_ix_new).alias("episode_index"),
            (pl.col("frame_index") + frame_counter).alias("index"),
        )
        ep_reix_fp = dsm_chunk_dir / f"episode_{ep_ix_new:06d}.parquet"
        ep_reix.write_parquet(ep_reix_fp)
        frame_counter += len(ep)
        ep_ix_new += 1

    print("\nMerge complete!")
    print(f"Total episodes created: {ep_ix_new}")
    print(f"Total frames (steps): {frame_counter}")
    return


@app.cell
def _(dsm_chunk_dir, pl):
    dsme11_path = dsm_chunk_dir / 'episode_000011.parquet'
    dsme11 = pl.read_parquet(dsme11_path)
    dsme11
    return


@app.cell
def _(dsm_chunk_dir, pl):
    dsme0_path = dsm_chunk_dir / 'episode_000000.parquet'
    dsme0 = pl.read_parquet(dsme0_path)
    dsme0
    return


@app.cell
def _(dsm_chunk_dir, pl):
    dsme1_path = dsm_chunk_dir / 'episode_000001.parquet'
    dsme1 = pl.read_parquet(dsme1_path)
    dsme1
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
