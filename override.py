class Field( object ):
    def __init__( self, a, b ):
        self.a = a
        self.b = b
        self.field = self.buildField()

    def buildField( self ):
        field = [0,0,0]
        return field

class Background( Field ):
    def __init__( self, a, b, c ):
        super(Background, self).__init__( a, b )
        self.field = self.buildField( c )

    def buildField( self, c ):
        field = [c]
        return field

a, b, c = 0, 1, 2
background = Background( a, b, c )
