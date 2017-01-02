s = '0ab12'#q#d5'


def comb(s):
	if not s:
		return [""]

	res = [s[0]]

	for i in xrange(1,len(s)):
		m = len(res)
		print i, res

		for j in xrange(m):
			
			if 97 <= ord(s[i]) <= 122:
				res.append(res[j] + s[i].upper())
			res[j]+=s[i]
	return res

print comb(s)