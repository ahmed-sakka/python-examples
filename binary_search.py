input = [1,2,3,4,5]

#pythonic way of doing recursive binary search but cant return back the index of the element -- returns only True/False
def binsearchr(arr, x):
    if len(arr) == 0:
        return False

    mid = (len(arr)-1)/2 #or len(arr)/2
    if arr[mid] == x:
        return True

    #no elif
    if arr[mid] > x:
        return binsearchr(arr[:mid], x)

    #no #else
    return binsearchr(arr[mid+1:], x)

#non-pythonic way of doing recursive binary search but returns back the index of the element
def binsearchr2(arr, l, r, x):
    if r >= l:
        mid = (l + r)/2
        
        if arr[mid] == x:
            return mid

        #no elif
        if arr[mid] > x:
            return binsearchr2(arr, l, mid-1, x)

        #no #else
        return binsearchr2(arr, mid+1, r, x)
    return False

#pythonic way of doing iterative binary search, returns back the index of the element
def binsearchi(arr, x):
   l = 0
   r = len(arr) - 1

   while r >= l:
      mid = (l + r)/2

      if arr[mid] == x:
        return mid

      if arr[mid] > x:
        r = mid - 1
      
      else:
        l = mid + 1    
   return False

#non-pythonic way of doing iterative binary search, returns back the index of the element
def binsearchi2(arr, l, r, x):
   while r >= l:
      mid = (l + r)/2

      if arr[mid] == x:
        return mid

      if arr[mid] > x:
        r = mid - 1
      
      else:
        l = mid + 1
   return False

print binsearchr(input, 5)
print binsearchr2(input, 0, len(input)-1, 5)
print binsearchi(input, 5)
print binsearchi2(input, 0, len(input)-1, 9)
