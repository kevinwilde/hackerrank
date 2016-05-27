import math
import re

class ClassData:
    def __init__(self):
        self.numdocs = 0
        self.features = {}
        self.sum_of_features = 0
        self.prior_prob = 0
        
    def add_feature(self, feat):
        if feat in self.features:
            self.features[feat] += 1
        else:
            self.features[feat] = 1
            
class NaiveBayes:
    def __init__(self, num_classes):
        self.classes = [ClassData() for _ in range(num_classes)]
        
    def tokenize(self, sText): 
        """Given a string of text sText, returns a list of the individual tokens that 
        occur in that string (in order)."""

        lTokens = []
        sToken = ""
        for c in sText:
            if re.match("[a-zA-Z0-9]", str(c)) != None or c == "\"" or c == "_" or c == "-":
                sToken += c
            else:
                if sToken != "":
                    lTokens.append(sToken)
                    sToken = ""
                if c.strip() != "":
                    lTokens.append(str(c.strip()))
               
        if sToken != "":
            lTokens.append(sToken)

        return lTokens
        
    def train(self):
        total_numdocs = 0
        with open('trainingdata.txt') as f:
            for line in f:
                total_numdocs += 1
                classnum = int(line[0])
                tokens = self.tokenize(line[2:])
                
                self.classes[classnum-1].numdocs += 1
                
                for i in range(len(tokens)):
                    unigram = tokens[i].lower()
                    self.classes[classnum-1].add_feature(unigram)
                    
        for i in range(len(self.classes)):
            self.classes[i].prior_prob = self.classes[i].numdocs / float(total_numdocs)
            self.classes[i].sum_of_features = sum([self.classes[i].features[k] for k in self.classes[i].features])
        
    
    def classify(self, sText):
        """Given a target string sText, this function returns the most likely
        document class to which the target string belongs"""
        
        lWordList = self.tokenize(sText)
        num_classes = len(self.classes)
        
        probabilities = [0 for _ in range(num_classes)]

        # Prior Probabilities
        for i in range(num_classes):
            probabilities[i] = math.log(self.classes[i].prior_prob)

        for i in range(len(lWordList)):
            unigram = lWordList[i].lower()

            for i in range(num_classes):
                word_freq = 1 + (self.classes[i].features[unigram] if unigram in self.classes[i].features else 0)
                probabilities[i] += math.log(float(word_freq) / self.classes[i].sum_of_features)
        
        best_class = 1
        best_prob = probabilities[0]
        for i in range(1, num_classes):
            if probabilities[i] > best_prob:
                best_prob = probabilities[i]
                best_class = i+1
                
        return best_class        
            
def main():
    b = NaiveBayes(num_classes=8)
    b.train()
    
    T = int(raw_input())
    for _ in range(T):
        doc = raw_input()
        print b.classify(doc)
    
if __name__ == '__main__':
    main()