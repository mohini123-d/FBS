def emp(**data):
    for key,val in data.items():
        print(f'{key} : {val}')

emp(id=101, name='Mohini',sal=40000)