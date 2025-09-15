from collections import defaultdict, deque


class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        available_supplies = set(supplies)
        # Map recipe to its index
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}
        # Map ingredient to recipes that need it
        dependency_graph = defaultdict(list)
        # Count of non-supply ingredients needed for each recipe
        in_degree = [0] * len(recipes)

        for recipe in recipes:
            for ingredient in ingredients[recipe_to_index[recipe]]:
                if ingredient not in available_supplies:
                    dependency_graph[ingredient].append(recipe)
                    in_degree[recipe_to_index[recipe]] += 1

        queue = deque([index for index, value in enumerate(in_degree) if value == 0])
        result = []
        while queue:
            current_recipe = queue.popleft()
            available_supplies.add(recipes[current_recipe])
            result.append(recipes[current_recipe])
            for dependency in dependency_graph[recipes[current_recipe]]:
                in_degree[recipe_to_index[dependency]] -= 1
                if in_degree[recipe_to_index[dependency]] == 0:
                    queue.append(recipe_to_index[dependency])

        return result


print(Solution().findAllRecipes(['a','b'], [['b'], ['a']], []))


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
