from collections import defaultdict


TRESHOLD = 500
item_counts = defaultdict(int)
pair_counts = defaultdict(int)
frequent_items = set()
frequent_pairs = set()


def normalizeGroup(*args):
	return str(sorted(args))


f = open('Online_Retail.csv', 'r')
lines = f.readlines()
f.close()


tx = defaultdict(list)
for i in range(1, len(lines)):
	data = lines[i].split(',')
	tx[data[0].strip()].append(data[2].strip())


#first pass............................................

#find candidate item
for tid in tx:
	for item in tx[tid]:
		item_counts[item] += 1

#filter for frequent items
for key in item_counts:
	if item_counts[key] >= TRESHOLD:
		frequent_items.add(key)

#show output
for item in frequent_items:
	print(item, ':', item_counts[item], 'Times')


#second pass............................................

#find candidate pair
for tid in tx:
	items = tx[tid]
	for idx1 in range(len(items)-1):
		if items[idx1] not in frequent_items:
			continue
		for idx2 in range(idx1+1, len(items)):
			if items[idx2] not in frequent_items:
				continue
			pair = normalizeGroup(items[idx1], items[idx2])
			pair_counts[pair] += 1

#filter frequent pairs
for key in pair_counts:
	if pair_counts[key] >= TRESHOLD:
		frequent_pairs.add(key)

for p in frequent_pairs:
	print(p + ": " + str(pair_counts[p]) + " times.")