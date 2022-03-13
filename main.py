from HW1.InvIndex import InvIndex

# load the documents
doc1 = open('doc1.txt', encoding='utf8')
read1 = doc1.read()
print(read1)
doc2 = open('doc2.txt', encoding='utf8')
read2 = doc2.read()
print(read2)
doc3 = open('doc3.txt', encoding='utf8')
read3 = doc3.read()
print(read3)
doc4 = open('doc4.txt', encoding='utf8')
read4 = doc4.read()
print(read4)
totaldoc = [doc1, doc2, doc3, doc4]
totalread = [read1, read2, read3, read4]
print(totalread)

# to obtain the number of lines in each documents
line = [1, 1, 1, 1]

for i in range(4):
    for word in totalread[i]:
        if word == '\n':
            line[i] += 1
    print("Number of lines in doc:", i + 1, " is: ", line[i])

new_invIdx = InvIndex()
invIdx = new_invIdx.new_index(totalread)
# ****************************************************************************************************************

query1 = 'sales rise'
query2 = 'sales increase in July'
query3 = 'home sales'
res1 = new_invIdx.search_index(query1)
print('The result for query 1 ('+query1+') is : ' + res1.__str__())
res2 = new_invIdx.search_index(query2)
print('The result for query 2 ('+query2+') is : ' + res2.__str__())
res3 = new_invIdx.search_index(query3)
print('The result for query 3 ('+query3+') is : ' + res3.__str__())

