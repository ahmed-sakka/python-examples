def break_while_loop_using_break_or_return(x):
    while True:
        if x%2 == 0:
            #break
            return
        else: 
            print x
            return

def break_for_loop_using_break_or_return(x):
    for i in range(x):
        if x%2 == 0:
            #break
            return
        else: 
            print x
            return

def return_stmt_optional():
    x = 0
    #return

break_while_loop_using_break_or_return(10)
break_while_loop_using_break_or_return(1)
break_for_loop_using_break_or_return(1)
return_stmt_optional()
