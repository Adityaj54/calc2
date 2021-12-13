class Results:


    @staticmethod
    def write_results(value_1,value_2,res,op):
        with open('result.txt','a') as file:
            file.write((','.join([value_1,value_2,res,op]))+'\n')

    @staticmethod
    def display_results():
        with open('result.txt','r') as file:
            list_res = []
            for line in file:
                list_res.append(line.split(','))
            return list_res

    @staticmethod
    def clear_results():
        with open('result.txt','r+') as f:
            f.truncate(0)





