class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(str)

        res = []
        for key, value in hash_map.items():
            res.append(value)
        
        return res
            
                
                