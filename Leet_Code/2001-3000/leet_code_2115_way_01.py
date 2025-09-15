from collections import defaultdict


class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        new_recipes = self.topological_sort(recipes, ingredients, supplies)
        new_ingredients = [recipes.index(i) for i in new_recipes]
        new_ingredients = [ingredients[i] for i in new_ingredients]
        possible = set(supplies)
        recipes_result = []
        for recipe, ingredient in zip(new_recipes, new_ingredients):
            if all(ing in possible for ing in ingredient):
                recipes_result.append(recipe)
                possible.add(recipe)
        return recipes_result

    def topological_sort(self,a, b, c):
        # Create a graph of dependencies
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for item, deps in zip(a, b):
            for dep in deps:
                if dep in a:
                    graph[dep].append(item)
                    in_degree[item] += 1

        # Initialize the queue with items that have no dependencies
        queue = [item for item in a if in_degree[item] == 0]
        result = []

        # Perform topological sort
        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)


        return result
    # def topological_sort(self,a, b, c):
    #     # Create a graph of dependencies
    #     graph = defaultdict(list)
    #     in_degree = defaultdict(int)
    #     for item, deps in zip(a, b):
    #         for dep in deps:
    #             if dep in a:
    #                 graph[dep].append(item)
    #                 in_degree[item] += 1
    #
    #     # Initialize the queue with items that have no dependencies
    #     queue = [item for item in a if in_degree[item] == 0]
    #     result = []
    #
    #     # Perform topological sort
    #     while queue:
    #         current = queue.pop(0)
    #         result.append(current)
    #         for neighbor in graph[current]:
    #             in_degree[neighbor] -= 1
    #             if in_degree[neighbor] == 0:
    #                 queue.append(neighbor)
    #
    #     # Check if there's a cycle
    #     if len(result) != len(a):
    #         return None  # Cycle detected
    #
    #     return result


print(Solution().findAllRecipes(
    ["xevvq", "izcad", "p", "we", "bxgnm", "vpio", "i", "hjvu", "igi", "anp", "tokfq", "z", "kwdmb", "g", "qb", "q",
     "b", "hthy"], [
        ["wbjr"],
        ["otr", "fzr", "g"],
        ["fzr", "wi", "otr", "xgp", "wbjr", "igi", "b"],
                    ["fzr", "xgp", "wi", "otr", "tokfq", "izcad", "igi", "xevvq", "i", "anp"],
        ["wi", "xgp", "wbjr"],
                    ["wbjr", "bxgnm", "i", "b", "hjvu", "izcad", "igi", "z", "g"], ["xgp", "otr", "wbjr"],
                    ["wbjr", "otr"], ["wbjr", "otr", "fzr", "wi", "xgp", "hjvu", "tokfq", "z", "kwdmb"],
                    ["xgp", "wi", "wbjr", "bxgnm", "izcad", "p", "xevvq"], ["bxgnm"], ["wi", "fzr", "otr", "wbjr"],
                    ["wbjr", "wi", "fzr", "xgp", "otr", "g", "b", "p"], ["otr", "fzr", "xgp", "wbjr"],
                    ["xgp", "wbjr", "q", "vpio", "tokfq", "we"], ["wbjr", "wi", "xgp", "we"], ["wbjr"], ["wi"]],
    ["wi", "otr", "wbjr", "fzr", "xgp"]))  # ["xevvq","izcad","bxgnm","i","hjvu","tokfq","z","g","b","hthy"]
print(Solution().findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]],
                                ["yeast", "flour", "meat"]))  # ["bread","sandwich"]
print(Solution().findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"]))  # ["bread"]
print(Solution().findAllRecipes(["bread", "sandwich", "burger"],
                                [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                                ["yeast", "flour", "meat"]))  # ["bread","sandwich","burger"]
