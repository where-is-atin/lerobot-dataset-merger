# TODO
## RUN (e2e)
- [ ] merge each
  - [ ] merge data
    - [x] what is chunks_size exactly
      """Max number of episodes per chunk."""
    - [x] tasks how merge?
      -
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
