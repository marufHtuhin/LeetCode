from collections import Counter
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        c=Counter()
        for i in cpdomains:
            cnt,domain=i.split()
            dom=domain.split(".")
            for j in range(len(dom)):
                c[".".join(dom[j:])]+=int(cnt)
        
        return [" ".join((str(l),k)) for k,l in c.items()]