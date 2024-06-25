class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  
        self.domains = domains      
        self.constraints = constraints  

    def is_consistent(self, var, assignment, neighbor, color):
        for (v1, v2) in self.constraints:
            if v1 == var and v2 == neighbor:
                if assignment[neighbor] == color:
                    return False
            elif v2 == var and v1 == neighbor:
                if assignment[neighbor] == color:
                    return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        var = next(v for v in self.variables if v not in assignment)
        for color in self.domains[var]:
            consistent = True
            for neighbor in self.variables:
                if (var, neighbor) in self.constraints or (neighbor, var) in self.constraints:
                    if neighbor in assignment and not self.is_consistent(var, assignment, neighbor, color):
                        consistent = False
                        break
            if consistent:
                assignment[var] = color
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                del assignment[var]
        return None
if __name__ == "__main__":
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {
        'WA': ['red', 'green', 'blue'],
        'NT': ['red', 'green', 'blue'],
        'SA': ['red', 'green', 'blue'],
        'Q': ['red', 'green', 'blue'],
        'NSW': ['red', 'green', 'blue'],
        'V': ['red', 'green', 'blue'],
        'T': ['red', 'green', 'blue']
    }
    constraints = [('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'), ('SA', 'Q'), ('SA', 'NSW'),
                   ('SA', 'V'), ('Q', 'NSW'), ('NSW', 'V')]
    csp = CSP(variables, domains, constraints)
    solution = csp.backtracking_search()
    if solution:
        print("Solution found:")
        for var in variables:
            print(f"{var}: {solution[var]}")
    else:
        print("No solution found.")
