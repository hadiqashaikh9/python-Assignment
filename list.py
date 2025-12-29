#add list items
#append()
subjectlist=["Eng","computer","Math"]
subjectlist.append ("Science")
print (subjectlist)
#insert()
subjectlist=["English","computer","Math"]
subjectlist.insert (2,"Science")
print (subjectlist)
#extend()
subjectlist=["English","computer","Math"]
subjectmarks=[54,68,39]
subjectlist.extend (subjectmarks)
print(subjectlist)



#remove list items
#remove
subjectlist=["ai","cn","ds"]
subjectlist.remove ("cn")
print (subjectlist)
#pop
subjectlist=["ai","cn","ds"]
subjectlist.pop (2)
print (subjectlist)
#delete
subjectlist=["ai","cn","ds"]
del subjectlist [1]
print (subjectlist)
#remove
subjectlist=["ai","cn","ds"]
subjectlist.clear ()
print (subjectlist)
