class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        s=set(dictionary)
        def root(word):
            for i in range(1,len(word)+1):
                pref=word[:i]
                if pref in s:
                    return pref
            return word
        words=sentence.split()
        replaced=[root(i) for i in words]
        return " ".join(replaced)