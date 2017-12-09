import math
import numpy as np
from collections import defaultdict, Counter


#Needs Float input
class TriangularMF:
    """Triangular fuzzy logic membership function class."""
    def __init__(self, name, start, top, end):
        self.name = name
        self.start = float(start)
        self.top = float(top)
        self.end = float(end)

    def calculate_membership(self, x):
        if x < self.start or x > self.end:
            return(0.0)
        if x < self.top:
            return (x-self.start)/(self.top-self.start)
        if x > self.top:
            return (self.end-x)/(self.end-self.top)
        if x == self.top:
            return 1.0
    
    def get_range(self):
        return(self.start, self.end)
        
#Needs Float input
class TrapezoidalMF:
    """Trapezoidal fuzzy logic membership function class."""
    def __init__(self, name, start, left_top, right_top, end):
        self.name = name
        self.start = float(start)
        self.left_top = float(left_top)
        self.right_top = float(right_top)
        self.end = float(end)

    def calculate_membership(self, x):
        if x < self.start or x > self.end:
            return 0.0
        if x < self.left_top:
            return (self.left_top-x)/(self.left_top - self.start)
        if x > self.right_top:
            return (self.end-x)/(self.end-self.right_top)
        if x >= self.left_top and x <= self.right_top:
            return 1.0

    def get_range(self):
        return(self.start, self.end)

# Test your implementation by running the following statements
# Enter your answers in the Google form to check them, round to two decimals

triangular_mf = TriangularMF("medium", 150, 250, 350)
print(triangular_mf.calculate_membership(100))
print(triangular_mf.calculate_membership(249))
print(triangular_mf.calculate_membership(300))

trapezoidal_mf = TrapezoidalMF("bad", 0, 0, 2, 4)
print(trapezoidal_mf.calculate_membership(1.2))
print(trapezoidal_mf.calculate_membership(2.3))
print(trapezoidal_mf.calculate_membership(3.9))

class Variable:
    """General class for variables in an FLS."""
    def __init__(self, name, range, mfs):
        self.name = name
        self.range = range
        self.mfs = mfs

    def calculate_memberships(self, x):
        """Test function to check whether
        you put together the right mfs in your variables."""
        return {
            mf.name : mf.calculate_membership(x)
            for mf in self.mfs
        }

    def get_mf_by_name(self, name):
        for mf in self.mfs:
            if mf.name == name:
                return mf

class Input(Variable):
    """Class for input variables, inherits 
    variables and functions from superclass Variable."""
    def __init__(self, name, range, mfs):
        super().__init__(name, range, mfs)
        self.type = "input"

class Output(Variable):
    """Class for output variables, inherits 
    variables and functions from superclass Variable."""
    def __init__(self, name, range, mfs):
        super().__init__(name, range, mfs)
        self.type = "output"

# Input variable for your income


low = TrapezoidalMF('low', 0, 0, 200, 400)
medium = TriangularMF('medium', 200, 500, 800)
high = TrapezoidalMF('high', 600, 800, 1000, 1000)


mfs_income = [low, medium, high, excellent]
income = Input("income", (0, 1000), mfs_income)

# Input variable for the quality
qbad = TrapezoidalMF('bad', 0, 0, 2, 4)
qmedium = TriangularMF('okay', 2.00, 5.00, 8.00)
qexcellent = TrapezoidalMF('amazing', 6.00, 8.00, 10.0, 10.00)

mfs_quality = [qbad, qmedium, qgood, qexcellent]
quality = Input("quality", (0, 10), mfs_quality)

# Output variable for the amount of money
mbad = TrapezoidalMF('low', 0, 0, 100, 250)
mmedium = TriangularMF('medium', 150, 250, 350)
mhigh = TrapezoidalMF('high', 250, 400, 500, 500)
mfs_money = [mbad, mmedium, mhigh]
money = Output("money", (0, 500), mfs_money)

inputs = [income, quality]
output = money

# Test your implementation by running the following statements
# Enter your answers in the Google form to check them, round to two decimals

print(income.calculate_memberships(489))
print(quality.calculate_memberships(6))
print(output.calculate_memberships(222))

class Rule:
    """Fuzzy rule class, initialized with an antecedent (list of strings),
    operator (string) and consequent (string)."""
    def __init__(self, n, antecedent, operator, consequent):
        self.number = n
        self.antecedent = antecedent
        self.operator = operator
        self.consequent = consequent
        self.firing_strength = 0

    def calculate_firing_strength(self, datapoint, inputs):
        fs = []
        for index, variable in enumerate(inputs):
#            print(index)
            memb_dict = (variable.calculate_memberships(datapoint[index]))
            fs.append(memb_dict[self.antecedent[index]])
        if self.operator == 'and':
            self.firing_strength = min(fs)
        if self.operator == 'or':    
            self.firing_strength = max(fs)
        return self.firing_strength

# Test your implementation by checking the following statements
# Enter your answers in the Google form to check them, round to two decimals

rule1 = Rule(1, ["low", "amazing"], "and", "low")
print(rule1.calculate_firing_strength([200, 6.5], inputs))
print(rule1.calculate_firing_strength([0, 10], inputs))

rule2 = Rule(2, ["high", "bad"], "and", "high")
print(rule2.calculate_firing_strength([100, 8], inputs))
print(rule2.calculate_firing_strength([700, 3], inputs))

rule3 = Rule(2, ["low", "amazing"], "and", "low")
rule4 = Rule(2, ["medium", "amazing"], "and", "low")
rule5 = Rule(2, ["low", "okay"], "and", "low")
rule6 = Rule(2, ["medium", "okay"], "and", "medium")
rule7 = Rule(2, ["high", "okay"], "and", "medium")
rule8 = Rule(2, ["low", "bad"], "and", "low")
rule9 = Rule(2, ["medium", "bad"], "and", "medium")
rule10 = Rule(2, ["high", "bad"], "and", "high")
rule11 = Rule(2, ["high", "amazing"], "and", "low")

from collections import Counter

class Rulebase:
    """The fuzzy rulebase collects all rules for the FLS, can
    calculate the firing strengths of its rules."""
    def __init__(self, rules):
        self.rules = rules

    def calculate_firing_strengths(self, datapoint, inputs):
        result = Counter()
        for i, rule in enumerate(self.rules):
            fs = rule.calculate_firing_strength(datapoint, inputs)
            consequent = rule.consequent
            if fs > result[consequent]:
                result[consequent] = fs
        return result

# Add the rules listed in the question description
rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11]

rulebase = Rulebase(rules)

# Test your implementation of calculate_firing_strengths()
# Enter your answers in the Google form to check them, round to two decimals

datapoint = [500, 3]
print(rulebase.calculate_firing_strengths(datapoint, inputs))

datapoint = [234, 7.5]
fs = (rulebase.calculate_firing_strengths(datapoint, inputs))
print(fs)
for i in fs:
    print(i)

class Reasoner:
    def __init__(self, rulebase, inputs, output, n_points, defuzzification):
        self.rulebase = rulebase
        self.inputs = inputs
        self.output = output
        self.discretize = n_points
        self.defuzzification = defuzzification

    def inference(self, datapoint):
        # 1. Calculate the highest firing strength found in the rules per 
        # membership function of the output variable
        # looks like: {"low":0.5, "medium":0.25, "high":0}        
        firing_strengths = (rulebase.calculate_firing_strengths(datapoint, self.inputs))
        print(firing_strengths)

        # 2. Aggragate and discretize
        # looks like: [(0.0, 1), (1.2437810945273631, 1), (2.4875621890547261, 1), (3.7313432835820892, 1), ...]
        input_value_pairs = self.aggregate(firing_strengths)
        
        # 3. Defuzzify
        # looks like a scalar
        crisp_output = self.defuzzify(input_value_pairs)
        return crisp_output

    def aggregate(self, firing_strengths):
        
        # First find where the aggrageted area starts and ends
        (start, end) = (-1, -1)
        for fs in firing_strengths:
            if firing_strengths[fs] > 0.0:
                mf = self.output.get_mf_by_name(fs)
                (s, e) = mf.get_range()
                if start == -1 or s <= start:
                    start = s
                if end == -1 or end <= e:
                    end = e
#        print(start, end)
        # Second discretize this area and aggragate      
        # Your code here
        step_size = (end-start)/(float(self.discretize) - 1.0)
        input_value_pairs = []
        while start <= end:
            memb = self.memb_of_agg(firing_strengths, start)
            input_value_pairs.append((start, memb))
            start += step_size
        return input_value_pairs
        

    def memb_of_agg(self, firing_strengths, x):
        strength = 0
        for fs in firing_strengths:
            mf = self.output.get_mf_by_name(fs)
            m = mf.calculate_membership(x)
            m = m*firing_strengths[fs]
            if m > strength:
                strength = m
        return strength

    def defuzzify(self, input_value_pairs):
        crisp = -1
        maximum = 0
        if self.defuzzification == 'som':
            for (i, v) in input_value_pairs:
                if v > maximum or crisp == -1:
                    crisp = i
                    maximum = v
        if self.defuzzification =='lom':
            for (i, v) in input_value_pairs:
                if v >= maximum or crisp == -1:
                    crisp = i
                    maximum = v
        return crisp

# Test your implementation of the fuzzy inference
# Enter your answers in the Google form to check them, round to two decimals

# thinker = Reasoner(rulebase, inputs, output, 201, "som")
# datapoint = [100, 1]
# print(round(thinker.inference(datapoint)))

# thinker = Reasoner(rulebase, inputs, output, 101, "lom")
# datapoint = [550, 4.5]
# print(round(thinker.inference(datapoint)))

# thinker = Reasoner(rulebase, inputs, output, 201, "som")
# datapoint = [900, 6.5]
# print(round(thinker.inference(datapoint)))

# thinker = Reasoner(rulebase, inputs, output, 201, "lom")
# datapoint = [100, 1]
# print(round(thinker.inference(datapoint)))

# thinker = Reasoner(rulebase, inputs, output, 101, "lom")
# datapoint = [550, 4.5]
# print(round(thinker.inference(datapoint)))

thinker = Reasoner(rulebase, inputs, output, 201, "lom")
datapoint = [900, 6.5]
print(round(thinker.inference(datapoint)))
