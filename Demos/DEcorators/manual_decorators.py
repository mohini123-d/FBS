def greet():
    print('Good morning....')

def myDecoretors(fun):
    print('this is decorators')
    fun()
    print('End of my decorators')


myDecoretors(greet)