#!/usr/bin/python3

import json

def get_style():
    with open('style.css', "r") as read_file:
        html = read_file.read()
    return html

def get_head():
    style = get_style()
    html = """<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
%s
</style>
""" % (style)
    return html

def get_inputs():
    html = """<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for key.." title="Type in a name"> 
"""
    return html

def get_script():
    html = "<script>"
    with open('code.js', "r") as read_file:
            html += read_file.read()
    html += "</script>"

    return html

def get_table(keys,col_list,data):
    html = '<table id="myTable">\n'
    html += '<tr class="header">\n'
 
    html += "<th>Key Value</th>\n"
    for col in col_list:
        #html += "<th style=\"width:30%%;\">%s</th>\n" % col
        html += "<th>%s</th>\n" % col
    html += "</tr>"
    for cur_key in keys:
        html += "<tr>\n"
        html += "<td>%s</td>\n" % cur_key
        for cur_col in col_list:
            html += "<td>%s</td>\n" % data[cur_key][cur_col]
        html += "</tr>\n"
    html += "</table>\n"
    return html


def get_body(unique_keys, col_list, table_data):
    title = 'Test Title'
    all_inputs = get_inputs()
            
    table = get_table(unique_keys,col_list,table_data)
    script = get_script()
    html = """ <h2>%s</h2>
    %s
    %s
    %s
""" % (title,all_inputs,table,script)
    return html

def get_html(unique_keys, col_list, table_data):
    head = get_head()
    body = get_body(unique_keys, col_list, table_data)

    html = """<!DOCTYPE html>
<html>
    <head>
    %s
    </head>
    <body>
    %s
    </body>
</html>
""" % (head,body)
    return html

def get_all_keys(data):
    result = []
    for key in data:
        result.append(key)
    return result

def build_table(file_list):
    all_data = {}
    result_data = {}
    unique_keys = []
    col_list = sorted(file_list)
    for filepath in file_list:
        with open(filepath, "r") as read_file:
            data = json.load(read_file)
            all_data[filepath] = data
            all_keys = get_all_keys(data)
            for k in all_keys:
                if k not in unique_keys:
                    unique_keys.append(k)

    for cur_key in unique_keys:
        result_data[cur_key] = {}
        for cur_col in col_list:    
            result_data[cur_key][cur_col] = 'NOT DEFINED'
            if cur_col in all_data:
                if cur_key in all_data[cur_col]:
                    result_data[cur_key][cur_col] = all_data[cur_col][cur_key]
    #print(all_data)
    #print(result_data)
    return sorted(unique_keys), col_list, result_data

def main():
    unique_keys, col_list, table_data = build_table(['file1.json', 'file2.json', 'file3.json','file4.json','file5.json',])
    print("Unique Keys:")
    print(unique_keys)
    print("Columns:")
    print(col_list)

    f = open('report.html','w+')
    f.write(get_html(unique_keys, col_list, table_data))
    f.close()

if __name__ == '__main__':
    main()
