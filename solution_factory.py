
class SolutionFactory:
    @staticmethod
    def create_solution(solution_type, helpers, solution=[]):
        from particle import Particle
        from genetic_solution import GeneticSolution
        from branch import Branch
        from annealing_solution import AnnealingSolution

        if solution_type == Particle:
            return Particle(helpers)
        
        if solution_type == GeneticSolution:
            if len(solution) > 0:
                return GeneticSolution(helpers, solution)
            
            return GeneticSolution(helpers)
        
        if solution_type == Branch:
            if len(solution) > 0:
                return Branch(helpers, solution)
            
            return Branch(helpers)
        
        if solution_type == AnnealingSolution:            
            return AnnealingSolution(helpers)