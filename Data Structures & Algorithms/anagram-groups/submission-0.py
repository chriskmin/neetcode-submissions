class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            empty_array = [0] * 26
            for char in string:   
                index = ord(char) - ord('a')
                empty_array[index] += 1
            key = tuple(empty_array)
            if key not in groups:
                groups[key] = []
                groups[key].append(string)
            else:
                groups[key].append(string)
        return list(groups.values())




        