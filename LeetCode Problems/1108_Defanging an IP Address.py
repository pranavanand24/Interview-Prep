class Solution:
    def defangIPaddr(self, address):
        return address.replace('.','[.]')