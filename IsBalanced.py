def check (expression):
    if(len(expression) == 0):
      return True
  
    open_tup = ('({[')
    close_tup = (')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []

    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return False

    if not queue:
        return True
    else:
        return False

#print (check("({)"))
