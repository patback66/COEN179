orig = [0 for x in range(0,32)]
for i in range(0,32):
    orig[i] = i
orig.reverse()
print orig

root1a = []
root1b = []

count = 0
while count < 32:
    root1a.append(orig[count])
    count += 1
    root1b.append(orig[count])
    count += 1
print "Root 1:"
print root1a
print root1b

root2aa = []
root2ab = []
count = 0
while count < 16:
    root2aa.append(root1a[count])
    count += 1
    root2ab.append(root1a[count])
    count += 1

root2ba = []
root2bb = []
count = 0
while count < 16:
    root2ba.append(root1b[count])
    count += 1
    root2bb.append(root1b[count])
    count += 1

print "Root 2:"
print root2aa
print root2ab
print root2ba
print root2bb

#next root


