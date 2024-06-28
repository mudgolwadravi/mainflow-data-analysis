#list operations
my_list=[11,22,33,44,55]
my_list.append(99)
my_list.remove(44)
my_list[0]=66
print("Updated list :",my_list)

#Dictionary operations
my_dict={'name':'ravi','age':21,'city':'hyd'}
my_dict['gender']='male'
del my_dict['city']
my_dict['name']='kumar'
print("Updated Dictionary:",my_dict)

#Set operations
my_set={1,2,3,4,5}
my_set.add(0)
my_set.remove(3)
my_set.discard(2)
my_set.add(7)
print("Updated Set:",my_set)

