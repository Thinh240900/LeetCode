from collections import defaultdict, deque


class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        available = set(supplies)

        # Queue to process recipe indices
        recipe_queue = deque(range(len(recipes)))
        created_recipes = []
        last_size = -1  # Tracks last known available count

        # Continue while we keep finding new recipes
        while len(available) > last_size:
            last_size = len(available)
            queue_size = len(recipe_queue)

            # Process all recipes in current queue
            while queue_size > 0:
                queue_size -= 1
                recipe_idx = recipe_queue.popleft()
                if all(
                        ingredient in available
                        for ingredient in ingredients[recipe_idx]
                ):
                    # Recipe can be created - add to available items
                    available.add(recipes[recipe_idx])
                    created_recipes.append(recipes[recipe_idx])
                else:
                    recipe_queue.append(recipe_idx)

        return created_recipes



print(Solution().findAllRecipes(['a','e'],[['e'], ['a']],['b','c']))

print(Solution().findAllRecipes(["bread", "sandwich", "burger"],
                                [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                                ["yeast", "flour", "meat"]))  # ["bread","sandwich","burger"]

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
