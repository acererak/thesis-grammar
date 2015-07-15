from random import *

class Grammar:

    # init
    #
    # Initializes a grammar. If specified, 'start' is used as 
    # the start string for a derivation performed by the
    # 'generate' method below.
    #
    # This is called when the instructor is invoked, for example
    # in the code
    #
    #   Gr = Grammar('<sentence>')
    #
    def __init__(self, start_string=None):
        pass

        self.start = start_string
        self.rules = { }

    # read
    #
    # Reads a grammar from a file with the given name.
    #
    def read(self, filename):

        file = open(filename,'r')
        line = file.readline()[:-1]
        while line != '':
            syms = line.split(' ')
            lhs = syms[0]
            rhs = ' '.join(syms[2:]) 
            self[lhs] = rhs
            line = file.readline()[:-1]

    # setitem
    #
    # Adds a production to the grammar, one of the form:
    #
    #    var ::= rhs
    #
    # var should be a variable string
    # rhs should be a string of variables and terminals
    #
    # This method is invoked when a 'component assignment'
    # is used in code, for example
    #
    #   Gr['<sentence>'] = '<noun_phrase> <verb_phrase>'
    #

    def __setitem__(self,var,rhs):
        
        # check to see if the left hand value (var) is already in the rules dictionary
        if var in self.rules:

            # append the new rhs to the var key
            self.rules[var].append(rhs)

        # if var is not in the dictionary...
        else:

            # create a new entry for it
            self.rules[var] = [rhs]


    # getitem
    #
    # Returns the right-hand side of a production for the variable.
    # If there are several productions whose LHS is var, then one
    # is chosen at random.
    #
    # var should be a variable string
    #
    # This method is invoked when a 'component access' is expressed
    # in code, for example
    #
    #   Gr['<sentence>']
    #
    # might return the string '<noun_phrase> <verb_phrase>'
    #

    def __getitem__(self,var):


        # check to see if the entry exists in the dictionary
        if var in self.rules:
            
            # then supply a random element from its list
            RHSs = self.rules[var]
            rlen = len(RHSs)
            r = int(random() * rlen)

            return RHSs[r]

        else:

            return var

    def generate(self):
        
        next = self.start
        last = None
        # repeatedly apply grammar to some expanded string
        while next != last:

            last = next
            next = self.applyTo(next)

        return next

    # applyTo
    #
    # Give back a string that results from applying some Grammar
    # production to each of the variables that occur in the 
    # string.
    #

    def applyTo(self,derived_string=None):

        #
        new_array = derived_string.split(' ') 

        l = len(new_array)

        for i in range (l):

            new_array[i] = self[new_array[i]]

        new_string = ' '.join(new_array)

        return new_string

