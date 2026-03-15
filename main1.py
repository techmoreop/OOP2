class employee:
    def __init__(self):
     print('Employee created')
    def __del__ (self):
       print('Destructor called')
def create_o():
    print('Making Object...')
    object = employee()
    print('Function end...')
    return object
print('calling create function')
object = create_o()
print('Program Ends here')
