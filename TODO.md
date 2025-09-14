# TODO
## RUN (e2e)
- [ ] merge each
  - [ ] merge data (ep.parquet)
    - [x] what is chunks_size exactly
      """Max number of episodes per chunk."""

    - [x] tasks how merge?
      - tasks are frame+episode-level, so can just retain col values
    - [x] index recalc
      - global counter, sort each file and recalc in total. maybe also efficient to only do one. unsure if order matters here.
    - [x] episode_index recalc
      - sorted per dataset and concat
  - [ ] merge videos
  - [ ] merge meta
- [ ] verify above by trying to train like a single dataset or something


## RIGHT
- [ ] .gitattributes and README.md
- [ ] package into nice classes
- [ ] test with multi-chunk bigger datasets
  - [ ] make a splitter- also round-trip test works...?
- [ ] tests to verify stats
- [ ] exactly see what needs to be matched before merging: prompts,robot_type,features etc need to match



## BELLS: PERF / PRETTY / USABILITY
- [ ] polars scan parquet / lazy
- [ ] sub-select episodes from each ds
- [ ] integrate with lerobot better: remove local dev, inherit / attribute style work with LeRobotDataset
- [ ] duckdb for faster? helps at all?
- [ ] cli or sdk insterface
