couleurs = ["trefle", "pique", "carreau", "coeur"]
nums = [str(n+1) for n in range(10)] + ["valet", 'dame', 'roi', 'as']
res = []
for couleur in couleurs:
	for num in nums:
		res.append(num + " de " + couleur)
with open('test.csv', 'w') as f:
	f.write("\n".join(res))
