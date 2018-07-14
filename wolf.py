import wolframalpha

def wolf(Q):
    inputt = Q
    app_id = ""  # wolframalpha app_id
    client = wolframalpha.Client(app_id)
    res = client.query(inputt)
    # print(res.result)
    try:
        answer = (next(res.results).text)

    except StopIteration:
        answer = ("Nothing from wolf")
    return answer