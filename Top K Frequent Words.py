freqCount = {}
        output = []
        for ele in words:
            if ele not in freqCount:
                freqCount[ele] = 0
            freqCount[ele] += 1


        while freqCount:
            curMaxWords = []
            curMaxFreq = max(freqCount.values())
            for key, val in freqCount.items():
                if val == curMaxFreq:
                    curMaxWords.append(key)
            curMaxWords.sort()

            for ele in curMaxWords:
                if k == 0:
                    return output
                output.append(ele)
                del freqCount[ele]
                k -= 1

        return output
