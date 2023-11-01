from section11_exi.data_define import Record


# class FileReader:
#     def read_data(self) -> list[Record]:
#         pass

class TextFileReader():
    def read_data(self) :
        list_1:list= []
        a=('2011-01-01', '4b34218c-9f37-4e66-b33e-327ecd5fb897', '1689', '湖南省')
        b=('2011-01-01', '5b6a6417-9a16-4243-9704-255719074bff', '2353', '河北省')
        c=('2011-01-01', 'ae240260-68a9-4e59-b4c9-206be4c08a8d', '2565', '湖北省')
        d=('2011-01-01', 'c833e851-880f-4e05-9de5-b547f5ffc5e1', '2877', '山东省')
        e=('2011-01-01', 'dd27e822-884c-4d20-a309-986f6a90e2b9', '947', '安徽省')
        f=('2011-01-01', '8e43e3c5-44bf-4219-8a59-f512607aeefe', '815', '河北省')
        g=('2011-01-01', 'b6882f5f-fb10-4210-9e45-288dd2239594', '1363', '广东省')
        l=('2011-01-01', 'fd5056a8-8223-4d02-9988-04e1b41a57e8', '2149', '江苏省')

        list_1.append(a)
        list_1.append(b)
        list_1.append(c)
        list_1.append(d)
        list_1.append(f)
        list_1.append(g)
        list_1.append(l)
        print(list_1)
        # return list_1

t=TextFileReader()
t.read_data()

# data_dict1={}
# for record in list_1:
#     # print(record.data)
#     # print(data_dict1.keys())
#     if record.data in data_dict1.keys():
#         # 当前日期已经有记录了，所以记录作累加
#         data_dict1[record.data]+=record.money
#     else:
#         data_dict1[record.data]=record.money
#
# print(data_dict1)