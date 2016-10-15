# http://www.tutorialspoint.com/json/json_python_example.htm
# this can be good for bringing in strict json data


import demjson
import pprint





f = demjson.decode_file('nytime-sample.json', encoding=None)
print type(f)
pprint.pprint(f)




# #Import to dict
# json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
#
# text = demjson.decode(json)
# print  type(text)




# # Export
# data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
# json = demjson.encode(data)
# print type(json)

