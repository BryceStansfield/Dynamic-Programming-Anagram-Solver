import functools
import itertools
from precomputation import precomputation

class Solver:
    def __init__(self, dictionary_name):
        # Mapping the space of problems to the space of partial solutions
        self.solution_dict = {}
        
        # Getting some precomputed information
        self.pretty_word_list, self.equiv_classes, self.class_contains, self.not_containing, self.min_letters, self.equiv_class_size = precomputation(dictionary_name)
        
        
    @functools.lru_cache(maxsize = None)
    def solve(self, word_tuple):
        if word_tuple == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
            return 1 # May change
        
        # Main solving code
        solutions = []
        num_solutions = 0
        for equiv_class in self.equiv_classes:
            new_class = tuple(map(lambda x, y: x-y, word_tuple, equiv_class))
            if all(i >= 0 for i in new_class):
                future_solutions = self.solve(new_class)
                if future_solutions >= 1:
                    solutions.append(equiv_class)
                    num_solutions += self.equiv_class_size[equiv_class] * future_solutions
        
        self.solution_dict[word_tuple] = solutions
        return(num_solutions)
        
        
    def list_solutions(self, word):
        word_tuple = tuple(map(lambda x: sum([char == x for char in word]), "abcdefghijklmnopqrstuvwxyz"))
        print("#solutions = ", self.solve(word_tuple))
        
        
        return None #self.solution_list_calc(word_tuple)
        
    @functools.lru_cache(maxsize = None)
    def solution_list_calc(self, word_tuple):
        if word_tuple == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0):
            return [""]
        
        # Putting them in a big list
        soln_list = []
        for equiv_class in self.solution_dict[word_tuple]:
            new_class = tuple(map(lambda x,y: x-y, word_tuple, equiv_class))
            soln_list += [i[0] + " " + i[1] for i in itertools.product(self.class_contains[equiv_class], self.solution_list_calc(new_class))]
        return soln_list
            
        
              
    
        
        
            
            
        
        
    

