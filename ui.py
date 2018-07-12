import wikipedia as wk
import wolframalpha

while True:
    inputt = input("Q:")

    try:
        app_id = "RE5P4L-Q6UJ4QR459"

        client = wolframalpha.Client(app_id)

        res = client.query(inputt)

        answer = (next(res.results).text)
        print(answer)
    except StopIteration:

        print(wk.summary(inputt, sentences=2))