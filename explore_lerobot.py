import marimo

__generated_with = "0.15.3"
app = marimo.App(
    width="medium",
    app_title="explore_lerobot",
    sql_output="polars",
)


@app.cell
def _():
    from lerobot.datasets.lerobot_dataset import LeRobotDataset, LeRobotDatasetMetadata
    from pathlib import Path
    import polars as pl

    ds_local_path = Path('./datasets/a-t-i-n/record-matchbox-1/')
    ds1 = LeRobotDataset(root=ds_local_path, repo_id='a-t-i-n/record-matchbox-1')
    ds1
    return ds_local_path, pl


@app.cell
def _(ds_local_path, pl):
    d = pl.read_parquet(ds_local_path / 'data/chunk-000/episode_000009.parquet')
    d
    return (d,)


@app.cell
def _(d, pl):
    d_fixed = d.with_columns(
        (pl.col('timestamp') * 1000).cast(pl.Duration(time_unit='ms'))
    )

    d_fixed
    return


@app.cell
def _():


    return


if __name__ == "__main__":
    app.run()
