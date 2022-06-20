flat_json = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
flat_yaml = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
recursion_json = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
recursion_yaml = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

plain_recursive_json = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

plain_flat_json = '''Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true'''

json_recursive_json = '''[
    {
        "status": "NESTED",
        "key": "common",
        "value": [
            {
                "status": "ADDED",
                "key": "follow",
                "value": "false"
            },
            {
                "status": "UNCHANGED",
                "key": "setting1",
                "value": "Value 1"
            },
            {
                "status": "DELETED",
                "key": "setting2",
                "value": 200
            },
            {
                "status": "CHANGED",
                "key": "setting3",
                "value": "true",
                "value2": "null"
            },
            {
                "status": "ADDED",
                "key": "setting4",
                "value": "blah blah"
            },
            {
                "status": "ADDED",
                "key": "setting5",
                "value": {
                    "key5": "value5"
                }
            },
            {
                "status": "NESTED",
                "key": "setting6",
                "value": [
                    {
                        "status": "NESTED",
                        "key": "doge",
                        "value": [
                            {
                                "status": "CHANGED",
                                "key": "wow",
                                "value": "",
                                "value2": "so much"
                            }
                        ]
                    },
                    {
                        "status": "UNCHANGED",
                        "key": "key",
                        "value": "value"
                    },
                    {
                        "status": "ADDED",
                        "key": "ops",
                        "value": "vops"
                    }
                ]
            }
        ]
    },
    {
        "status": "NESTED",
        "key": "group1",
        "value": [
            {
                "status": "CHANGED",
                "key": "baz",
                "value": "bas",
                "value2": "bars"
            },
            {
                "status": "UNCHANGED",
                "key": "foo",
                "value": "bar"
            },
            {
                "status": "CHANGED",
                "key": "nest",
                "value": {
                    "key": "value"
                },
                "value2": "str"
            }
        ]
    },
    {
        "status": "DELETED",
        "key": "group2",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "status": "ADDED",
        "key": "group3",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]'''

json_flat_json = '''[
    {
        "status": "DELETED",
        "key": "follow",
        "value": "false"
    },
    {
        "status": "UNCHANGED",
        "key": "host",
        "value": "hexlet.io"
    },
    {
        "status": "DELETED",
        "key": "proxy",
        "value": "123.234.53.22"
    },
    {
        "status": "CHANGED",
        "key": "timeout",
        "value": 50,
        "value2": 20
    },
    {
        "status": "ADDED",
        "key": "verbose",
        "value": "true"
    }
]'''