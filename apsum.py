class Solution:
	def sum_of_ap(self, n, a, d):
		if n==1:
		    return a
		return a+(n-1)*d+self.sum_of_ap(n-1,a,d)