import wolframalpha

inputt = input("Question: ")
app_id = "RE5P4L-Q6UJ4QR459"

client = wolframalpha.Client(app_id)

res = client.query(inputt)

# print(res.result)


try:

    answer = (next(res.results).text)
    print(answer)
except StopIteration:
    print("No results")