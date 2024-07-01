class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        output = []
        for i in range(1, len(searchWord) + 1):
            result = []
            sub_query = searchWord[0:i]
            for word in products:
                if word.startswith(sub_query):
                    result.append(word)
            output.append(result[0:3])
        return output
