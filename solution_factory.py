
class SolutionFactory:
    @staticmethod
    def create_solution(solution_type, helpers, solution=[]):
        from particle import Particle
        from genetic_solution import GeneticSolution
        from branch import Branch
        from branch_mod import Branch_Mod
        from annealing_solution import AnnealingSolution

        if solution_type == Particle:
            if len(solution) > 0:
                return Particle(helpers, solution)
            
            return Particle(helpers)
        
        if solution_type == GeneticSolution:
            if len(solution) > 0:
                return GeneticSolution(helpers, solution)
            
            return GeneticSolution(helpers)
        
        if solution_type == Branch:
            if len(solution) > 0:
                return Branch(helpers, solution)
            
            return Branch(helpers)
        
        if solution_type == Branch_Mod:
            if len(solution) > 0:
                return Branch_Mod(helpers, solution)
            
            return Branch_Mod(helpers)
        
        if solution_type == AnnealingSolution:  
            if len(solution) > 0:
                return AnnealingSolution(helpers, solution)          
            return AnnealingSolution(helpers)