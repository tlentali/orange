# operations_research

<p align="center"> 
<img src="https://raw.githubusercontent.com/tlentali/operations_research/master/misc/casey_studio.jpg>
</p>

>The best solutions are often simple, yet unexpected.  
>J. Casablancas

## First, get some solvers

GLPK :

```
$ sudo apt-get install python-glpk
$ sudo apt-get install glpk-utils
```

Coin OR :

```
$ sudo apt-get install coinor-cbc
```

## Then, install PulP

Pulp is a wrapping library that generates input files for various LP solvers.

```
$ sudo pip install pulp
$ pulptest
```

