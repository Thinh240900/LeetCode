class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow),word)

        def solve(query):
            if query in words_perfect:
                return query

            queryLow = query.lower()
            if queryLow in words_cap:
                return words_cap[queryLow]

            queryVow = devowel(queryLow)
            if queryVow in words_vow:
                return words_vow[queryVow]
            return ''

        return map(solve, queries)

print(Solution().spellchecker(wordlist=["KiTe", "kite", "hare", "Hare"],
                              queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet",
                                       "keto"]))  # ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

print(Solution().spellchecker(wordlist=["yellow"], queries=["YellOw"]))  # ["yellow"]
