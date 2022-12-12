list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list = []
def flatten(l):
    for sublist in l:
        if type(sublist) == list:
            flatten(sublist)
        else:
            flatten_list.append(sublist)
    return flatten_list

print(flatten(list1))







list1 = [[1, 2], [3, 4], [5, 6, 7]]  

def liste(l):
  l.reverse()
  for r in (l):
    if type(r) == list:
      liste(r)
liste(list1)
print(list1)
  
