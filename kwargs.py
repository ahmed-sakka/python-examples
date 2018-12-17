def func(a, b=0):
    print a

func(**{'a': 1})
func(**{'b': 1})
kwargs = {'a': 1}
func(**kwargs)
