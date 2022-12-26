import sys
import numpy as np
import timeit
import os
import math
import subprocess
from subprocess import Popen, PIPE, STDOUT
import timeit


VERBOSITY=True
RUNSOLVER=True
SOLVERPATH='./kissat-bin'
start = timeit.default_timer()

    
    
#Each variable is assciated to an integer variable i > 0
#The literals associated to i are i and -i
#A clause is a list of literals
class model:
    name = ""
    #The number of variables 
    vars = 0
    #The set of (hard) clauses 
    cls = []
    #The set of (soft) clauses 
    soft = []
    #declare a new list of boolean bariables
    def define_new_list (self,size) :
        init = self.vars+1
        self.vars += size
        return [i for i in range (init,self.vars +1)]
    
    def print_my_model(self) : 
        if VERBOSITY : 
            print ('c Model\'s Name : ' , self.name)
            print ('c number of variables' , self.vars)
            print ('c The list of hard clauses: ' ) 
            for c in self.cls : 
                print (c
                      ) 
            if len(self.soft) >0 : 
                print ('c The list of soft clauses: ' )
                for c in self.soft : 
                    print (c) 

#write a cnf in a file
def write_cnf_file(clause_database, variables, file) :
    f = open(file, "w")
    f.write ("c generated from code\n")
    f.write ('p cnf ' + str(variables) + ' '  + str(len (clause_database) ) + '\n')
    for c in clause_database:
        f.write(c + '\n')
    f.close()
                    
    
#write a w-cnf in a file
def write_wcnf_file(clause_database,  soft_clause_database, variables, file) :
    f = open(file, "w")
    f.write ("c generated from code\n")
    top = len (soft_clause_database)
    f.write ('p wcnf ' + str(variables) + ' '  + str(len (clause_database)+ top  ) + ' '  + str(top +1 ) + '\n')
    top += 1
    for c in clause_database:
        f.write( str(top) + ' ' +  c + '\n')
    for c in soft_clause_database:
        f.write('1 ' + c + '\n' )
    f.close()



#return the clause defined by the sequence of literals seq_literals
def encode_clause (seq_literals) :
    cls= ''
    for i in seq_literals:
        cls+= str(i) + ' '
    cls += ' 0'
    return cls

#return the clause a --> clause
def encode_implication_clause (a,clause ) :
    return (str(-a) + ' ' + clause  )

#return the clause a --> b
def encode_implication (a,b) :
    return (str(-a) + ' ' + str(b) + ' 0' )


#force a to be true 
def always_true (a) :
    return (str(a) + ' ' + ' 0' )


#force a to be false 
def always_false (a) :
    return (str(-a) + ' ' + ' 0' )


#At most one is true 
def encode_atmost_one (m,x) : 
    l=len(x)
    for i in range (l):
        for k in range(i+1,l): 
            m.cls.append(encode_implication (x[i] , -x[k]))



#encode sum of x_ >= k in the model m
def encode_sum_at_least (m,x,k):
    #if k =1 then use disjunction
    assert (k>1)
    y=[]
    
    for j in range(k+1):
        y.append(m.define_new_list(len(x)))
    #To Complete Below 
    
    return y

    
#print the solution values of a given list of variables
def print_solution_values(sol,variables) : 
    for x in variables: 
        v=1
        if sol[x-1]<0 : 
            v=0
        print (' ' + str(v)  , end = '')
    
    print()
    
    
#print the solution value of a given variable
def value_of(sol,variable) : 
        v=1
        if sol[variable-1]<0 : 
            v=0
        return v
    

    
    
def run_solver(outputfile)    :
    if not RUNSOLVER:
        exit()
    else :
        if VERBOSITY : 
            stop = timeit.default_timer()
            print('d GENERATIONTIME', "%.2f" % (stop - start))
            print('c Solving the instance ..')
        outputsolutionfile = outputfile[:len(outputfile) - 4]
        outputsolutionfile=outputsolutionfile+'.sol'
        with open(outputsolutionfile, "w+") as f:
            subprocess.run([SOLVERPATH , outputfile  ] , stdout=f)

    sol = []

    with open(outputsolutionfile, 'r') as fp:
        for line in fp:
            if "UNSATISFIABLE" in line:
                fp.close()
                exit()
            elif line[0]== 'v':
                #[ 1:] )
                sol +=  [int(x) for x in line.split()[1:] ]
    fp.close()
    return sol


