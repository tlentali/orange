# orange

<p align="center">
  <a href="#"><img src="./misc/orange.jpg"  width="350"/></a>
</p>

Problem solver with [pulp](https://github.com/coin-or/pulp).

## Why ?

>The best solutions are often simple, yet unexpected.  
>**J. Casablancas**

## Installation
### First, get some solvers

GLPK :

```
$ sudo apt-get install python-glpk
$ sudo apt-get install glpk-utils
```

Coin OR :

```
$ sudo apt-get install coinor-cbc
```

### Then, install PulP and other libraries

Pulp is a wrapping library that generates input files for various LP solvers.

```
$ pip install -r requirement.txt
$ pulptest
```

