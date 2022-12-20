from sexpdata import loads, dumps


data = [
    False,
    {
        'important': [
            False,
            'present',
            False,
            -160032794,
            1046976520.3869586,
            -338325622
        ],
        'though': False,
        'probably': 459990107.0794139,
        'lost': 380213303.1942949,
        'treated': 'speak',
        'hearing': False
    },
    'using',
    -792082316.7501206,
    -475921153,
    -1098215464.3465562
]


def sexp(data):
    d = dumps(data, str_as='string', tuple_as='list', true_as='#t', false_as='#f', none_as='none')
    ind = 0
    in_dict = False
    result = ''

    for i in d.split(' '):
        if in_dict:
            result += ' '
            in_dict = False
        else:
            result += '\n' + '\t' * ind
            if ':' in i[:2]:
                in_dict = True
        if i[0] == '(':
            ind += 1
            result += '(' + '\n' + '\t' * ind + i[1:]
        elif i[-1] == ')':
            ind -= 1
            result += i[:-1] + '\n' + '\t' * ind + ')'
        else:
            result += i
    return result


import dicttoxml
import xml.dom.minidom


xml_data = dicttoxml.dicttoxml(data)
dom = xml.dom.minidom.parseString(xml_data)
print(dom.toprettyxml())
