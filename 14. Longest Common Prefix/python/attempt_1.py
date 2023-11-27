from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(f"longestCommonPrefix: {strs}")
        # as strs is defined as 1 <= strs.length <= 200
        lp = strs[0]

        for idx1, str1 in enumerate(strs):
            print("idx1: ", idx1)
            str_length = len(str1)

            shortest_str_length = len(lp)

            if str_length < shortest_str_length: # update shortest_str_length if the current string's length is smaller
                shortest_str_length = str_length

            print("lp: ", lp)
            print("shortest_str_length: ", shortest_str_length)

            lp_index = shortest_str_length # the index of lp where it should be sliced
            for idx2 in range(0, shortest_str_length):
                print(idx2)
                print(str1[idx2])
                print(lp[idx2])
                if str1[idx2] != lp[idx2]:
                    lp_index = idx2
                    break

            lp = lp[0: lp_index]

            if lp_index == 0: # indicate there is no lp between str1 and existing lp
                break

        print(f"final lp: {lp}")
        return lp
