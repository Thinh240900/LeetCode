from collections import defaultdict, deque


class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            # Already processed and can be made
            if can_make.get(recipe, False):
                return True

            # Not a valid recipe or cycle detected
            if recipe not in recipe_to_idx or recipe in visited:
                return False

            visited.add(recipe)

            # Check if all ingredients can be made
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )

            return can_make[recipe]

        # Process each recipe and collect those that can be made
        return [recipe for recipe in recipes if _check_recipe(recipe, set())]

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
