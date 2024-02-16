def function(input_str):
    try:
        input_str[0]= input_str[1]
        print(input_str)
    except NameError:
            print(1)

            try:function("Infosys")
            except:
                print(2)
