def person(name,**kwlargs):
    print("name:",name)
    for k,v in kwlargs.items():
        print(k , ":" , v)
person(name="Saiprasad",age=21,year="TY",language="Python")