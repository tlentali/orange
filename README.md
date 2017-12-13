# operations_research

![alt text](https://raw.githubusercontent.com/tlentali/operations_research/master/misc/casey_studio.jpg "Neistat studio NYC")


## First, get some solvers

GLPK :

```
$ sudo apt-get install python-glpk
$ sudo apt-get install glpk-utils
```

Coin OR :

```
sudo apt-get install coinor-cbc
```

## Then, install PulP

Pulp is a wrapping library that generates input files for various LP solvers.

```
$ sudo pip install pulp
$ pulptest
```

