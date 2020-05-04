def precomputation(dictionary_name):
    """Upon taking in the file name of an english word list, returns the following precomputed information:
       i) A pretty word list, formatted to be all lowercase
       ii) A dictionary, mapping a tuple of the number of each letter in a word to a unique id for this equivilance class. (Needs rephrasing)
       iii) A dictionary, mapping an equivilance class to its members
       iv) A length 26 list of sets, each containing the set of equivilance classes not containing the ith letter of the (English) alphabet. (0 being 'a')
       v) A length 26 list of integers, each containing the minimum number of letters a word containing the ith (English) letter contains.
       vi) A dictionary giving the size of every equivilance class"""
    pretty_word_list = []
    equiv_classes = {}
    equiv_class_size = {}
    class_contains = {}
    not_containing = [set() for i in range(0, 26)]
    min_letters = [float("inf") for i in range(0, 26)]
    
    with open(dictionary_name, "r") as f:
        i = 0
        for line in f:
            cur_word = line.strip().lower()
            pretty_word_list.append(cur_word)
            
            # Finding the words equivilance class
            equiv_class = tuple(map(lambda x: sum([char == x for char in cur_word]), "abcdefghijklmnopqrstuvwxyz"))
            
            if equiv_class not in equiv_classes:
                equiv_classes[equiv_class] = len(equiv_classes)
                class_contains[equiv_class] = [cur_word]
                equiv_class_size[equiv_class] = 1
            
                # Constructing iv) and v)
                for char_index in range(0, 26):
                    if chr(97+char_index) in cur_word:
                        # iv)
                        if len(cur_word) <= min_letters[char_index]:
                            min_letters[char_index] = len(cur_word)
                    else:
                        # v)
                        not_containing[char_index].add(len(equiv_classes)-1)
            else:
                # vi)
                equiv_class_size[equiv_class] += 1
                # ii)
                class_contains[equiv_class].append(cur_word)
            
            i += 1
            
    
    return pretty_word_list, equiv_classes, class_contains, not_containing, min_letters, equiv_class_size