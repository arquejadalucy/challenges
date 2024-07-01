'''
Given an array of strings, group the strings that are composed by the same
characters, returning an array of arrays.   t

For example, given:
["124", "412", "425", "241", "524", "324", "2141"]

Return:
[
    ["241", "124","412"],
    ["524","425"],
    ["324"],
    ["2141"]
]
'''

#MINHA RESPOSTA
def group_by_characters(arr: list[str]):
    result = []
    current = 0
    while current < len(arr):
        result.append([arr[current]])  # [["124"]] -> ["124"] -> "124"
        for i in range(0, len(arr) - 1):
            if sorted(arr[i]) == sorted(result[current][0]):
                result[current].append(arr[i])  # [["124", "412"]]
        current += 1
    return result


def group_by_characters_refactored(arr: list[str]):
    result = []
    current = 0
    current_list = []
    while current < len(arr):
        if arr[current] not in current_list:
            current_list = [arr[current]]  # [["124"]] -> ["124"] -> "124"
            for i in range(0, len(arr) - 1):
                if sorted(arr[i]) == sorted(current_list[0]):
                    current_list.append(arr[i])  # [["124", "412"]]
            result.append(current_list)
            current_list = []
            current += 1

    return result


# using dictionaries it would be optimal
breakpoint()
result = group_by_characters_refactored(["124", "412", "425", "241", "524", "324", "2141"])
print(result)
