def dataclean(input_list):
    # filte out error value
    clean_data = []
    for i in input_list:
        try:
            m = int(i)
            
        except ValueError:
            continue
        clean_data.append(m)
    clean_data.sort()
    
    return clean_data