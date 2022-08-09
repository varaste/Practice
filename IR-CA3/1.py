
from mrjob.job import MRJob
from mrjob.step import MRStep
from itertools import tee
import re
import sys

WORD_RE = re.compile(r"[\w']+")


class MRWordProbability(MRJob):
    
       def steps(self):
        return [
            # Pull strings out of the csv
            MRStep(mapper=self.mapper_pull_csv),
            # Produce bigrams from the string
            MRStep(mapper=self.mapper_get_bigrams,
                   combiner=self.combiner_count_bigrams,
                   reducer=self.reducer_count_bigrams),
            # Calculate percents and most common occurences
            MRStep(reducer=self.reducer_calculate_percents)
        ]
    

    def mapper_pull_csv(self, _, line):
        if(line[0] != '"'):
            yield (None, line[line.find(","):].lower())

    def mapper_get_bigrams(self, _, line):
        prevWord = ""
        # Use regex to find words
        for word in WORD_RE.findall(line):
            if(prevWord != ""):
                yield ((prevWord, word), 1)
            prevWord = word
    
    def combiner_count_bigrams(self, word, counts):
        yield (word, sum(counts))
    
    def reducer_count_bigrams(self, word, counts):
        first_word, second_word = word
        yield first_word, (sum(counts), second_word)
        
    def mostUsed(self, x):
        num, word = x
        return num
    
    def reducer_calculate_percents(self, word, pairs):
        
        total = 0
        
        pairs, secondPairs = tee(pairs)
        pairs, sortedPairs = tee(pairs)
        
        for pair in pairs:
            tmpCnt, _ = pair
            
            total = total + tmpCnt
        
        probabilityList = sorted(secondPairs, key=self.mostUsed, reverse = True)
        for anotherPair in probabilityList:
            word_count, word_key = anotherPair
            
            yield (word, word_key), ((float(word_count) / total), word_count)
        
        if (word == "my"):
            for i in range(10):
                if i == len(probabilityList): 
                    break
                word_count, word_key = probabilityList[i]
                yield 'Most used number ' + str(i+1), ((word, word_key), word_count / total, word_count)
              

# Run the program
if __name__ == '__main__':
    MRWordProbability.run()