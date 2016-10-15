# http://pymotw.com/2/json/
import json
import pprint




# --- Import json from file ---#

with open('nytime-sample.json', 'r') as handle:
    parsed = json.load(handle)
    # print json.dumps(parsed, indent=4, sort_keys=True)



# --- Goal #1 ---#
# Makes a list of dictionaries, where the dictionary key is "section" and value is "title"
##########################################################################################
    list_of_dic = []
    for i in parsed:
        list_of_dic.append(i['section'])

    #print list_of_dic


# --- Goal #3 ---#
# list of URLs for all media entries with "format": "Standard Thumbnail"
########################################################################

    # Find single instance
    # list_of_url = parsed[1]['media'][0]['media-metadata'][0]['format'] == 'Standard Thumbnail'

    list_of_url = []

    for i in parsed:  # type(i): dict type
        for ii in i['media']: # type(ii): dict type
            for iii in ii["media-metadata"]: # type(iii): dict type
                    if iii["format"] == "Standard Thumbnail":
                        list_of_url.append(iii["url"])


    pprint.pprint(list_of_url)
