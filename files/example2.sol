c ---- [ banner ] ------------------------------------------------------------
c
c Kissat SAT Solver
c 
c Copyright (c) 2021-2022 Armin Biere University of Freiburg
c Copyright (c) 2019-2021 Armin Biere Johannes Kepler University Linz
c 
c Version 3.0.0 97917ddf2b12adc6f63c7b2a5a403a1ee7d81836
c Apple clang version 14.0.0 (clang-1400.0.29.102) -W -Wall -O3 -DNDEBUG
c Sat Dec 10 11:11:30 CET 2022 Darwin guns.laas.fr 21.6.0 arm64
c
c ---- [ parsing ] -----------------------------------------------------------
c
c opened and reading DIMACS file:
c
c   ./files/example2.cnf
c
c parsed 'p cnf 63 3' header
c closing input after reading 51 bytes
c finished parsing after 0.00 seconds
c
c ---- [ solving ] -----------------------------------------------------------
c
c  seconds switched rate      trail variables
c         MB reductions conflicts glue remaining
c          level restarts redundant irredundant
c
c *  0.00  0 0 0 0  0 0   0   0 0% 0  0  0 0%
c {  0.00  0 0 0 0  0 0   0   0 0% 0  0  0 0%
c }  0.00  0 0 0 0  0 0   0   0 0% 0  0  0 0%
c 1  0.00  0 0 0 0  0 0   0   0 0% 0  0  0 0%
c
c ---- [ result ] ------------------------------------------------------------
c
s SATISFIABLE
v -1 -2 -3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
v 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
v 53 54 55 56 57 58 59 60 61 62 63 0
c
c ---- [ profiling ] ---------------------------------------------------------
c
c           0.00   14.74 %  search
c           0.00   11.05 %  parse
c           0.00    6.32 %  focused
c           0.00    0.00 %  simplify
c =============================================
c           0.00  100.00 %  total
c
c ---- [ statistics ] --------------------------------------------------------
c
c conflicts:                                0                0.00 per second
c decisions:                                0                0.00 per conflict
c propagations:                             3             2117    per second
c
c ---- [ resources ] ---------------------------------------------------------
c
c maximum-resident-set-size:       1392508928 bytes       1328 MB
c process-time:                                              0.00 seconds
c
c ---- [ shutting down ] -----------------------------------------------------
c
c exit 10
