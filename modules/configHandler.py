def config(service, element):
    import json

    with open('../config.json') as config:
        data = json.load(config)
    return (data[service][element])