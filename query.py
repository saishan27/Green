import wikipedia as wk
import wolframalpha


def what(inputt):

    try:
              app_id = "RE5P4L-Q6UJ4QR459" #use ur own app id

              client = wolframalpha.Client(app_id)

              res = client.query(inputt)

              answer ="wolf: "+(next(res.results).text)

    except StopIteration:

              answer ="wiki: "+(wk.summary(inputt, sentences=1))

    return answer


