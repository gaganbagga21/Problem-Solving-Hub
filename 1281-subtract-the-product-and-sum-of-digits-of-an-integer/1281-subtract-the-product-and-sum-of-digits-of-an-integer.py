class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=n
        add=0
        mul=1
        while temp>0:
            r=temp%10
            add+=r
            mul*=r
            temp//=10
        return mul-add