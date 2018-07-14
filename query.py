import wikipedia as wk
import wolframalpha
import pyttsx3


def what(inputt):
    engine = pyttsx3.init()

    try:
              app_id = "RE5P4L-Q6UJ4QR459" #use ur own app id

              client = wolframalpha.Client(app_id)

              res = client.query(inputt)

              answer ="wolf: "+(next(res.results).text)
              engine.say("the answer is "+answer)
              engine.runAndWait()
    except StopIteration:

              answer ="wiki: "+(wk.summary(inputt, sentences=2))
              engine.say("wiki says"+answer)
              engine.runAndWait()
    return answer


