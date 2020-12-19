# dict of specific phrases
phrases = {
        "music_phrases" : ["play", "jam some"],
        "time_phrases"  : ["time", "clock"],
        "close_phrases" : ["kill", "close", "stop"],
        "wiki_phrases"  : ["wikipedia", "tell me about", "need info on"],
        "info_phrases"  : ["who is", "who the hell is", "who the heck is"],
        "joke_phrases"  : ["joke", "funny", "lighten me up", "make my day"],
        "hello_phrases" : ["say hello to", "greet", "be a gentleman to"],
        "news_phrases"  : ["news", "new", "what's up"],
        "alpha_phrases" : ["ask", "question", "compute", "calculate", "what is"]]
        }

# list of all supported phrases for checking
PHRASES = [p for l in phrases.values() for p in l]

