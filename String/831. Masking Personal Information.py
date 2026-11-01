class Solution(object):
    def maskPII(self, s):
        """
        :type s: str
        :rtype: str
        """
        if '@' and '.' in s:
            f=s.index('@')
            final=s[0].lower()+'*****'+s[f-1].lower()+s[f:].lower()
        else:
            f=''
            for i in s:
                if i.isalnum():
                    f+=i
            n=len(f)
            if n==10:
                final=('***-***-'+f[-4:])
            elif n==11:
                final=("+*-***-***-"+f[-4:])
            elif n==12:
                final=("+**-***-***-"+f[-4:])
            elif n==13:
                final=("+***-***-***-"+f[-4:])
        return final