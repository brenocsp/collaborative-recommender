# Funk SVD Recommender
Collaborative product recommender for the recommender system course at UFMG. This recommender is based on Simon Funk SVD recommender for the Netflix Prize. 

# How to run

Simply pass `main.py` to the python interpreter, and the program should start. You should pass the ratings and targets csv files on the command line.

In linux:

```shell
python3 main.py datasets/ratings.csv datasets/targets.csv
```

In Windows:

```shell
python main.py datasets/ratings.csv datasets/targets.csv
```
