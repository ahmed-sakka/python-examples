import re
import inspect

class MyClass :

    def __init__(self) :
        pass

    def private_function ( self ) :
        try :
            #function_call = inspect.stack()[1][4][0].strip()
            inspect.stack()

            # See if the function_call has "self." in the begining
            matched = re.match( '^self\.', function_call )
            if not matched :
                print 'This is Private Function, Go Away'
                return
        except :
            print 'This is Private Function, Go Away'
            return

        # This is the real Function, only accessible inside class #
        print 'Hey, Welcome in to function'

    def public_function ( self ) :
        # i can call private function from inside the class
        self.private_function()

c = MyClass()
c.public_function()
c.private_function()
