'''
This example demosntrates how to convert a dictionary of keys, duplicated values into
a new dictionary with unique keys, and a list of values for each key.

This exersice shows how to overcome the problem of having multiple entries for the same value, then using the unique values as keys in a new dictionary.
'''
def group_by_owners(files):
    authors = list(set(files.values()))                     #get authors (values) from dictionary ... use "set" to avoid duplicates .. convert back to list.                          
    files_names = (list(files.keys()))                      #get files names (keys) from dictionary
    res_dict = {}                                           #creat empty rsult dictionary for output
    for author in authors:                                  #loop over authors (values of dictionary)
        for i in range(len(files_names)):                   #loop over files names (keys of dictionary)
            if author==list(files.values())[i]:             #boolean to pick out files for current owner loop
                temp_list = [files_names[i]]                #create temporary list to hold file/files for each author
                if author in res_dict:                      #if the author is already in the output dictionary; then add the new file to the existing dictionary entry
                    res_dict[author].append(files_names[i]) #add the new file
                else:                                       #if the author is not in the output dictionary; then add it
                    res_dict[author] = temp_list            #make a new entry
    return res_dict

files = {
'math.txt': 'Sam',
'Eng101.txt':'Edward',
'biology.py': 'Sam',
'science.txt': 'James',
'calculus2.txt':'James',
'Fatigue.txt':'Jerry'

}

print(group_by_owners(files))