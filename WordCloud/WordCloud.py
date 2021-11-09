from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import pandas as pandas

new_file = pandas.read_csv(r"pakistan.csv", encoding = "latin-1")
comment_words = ''
stopwords = set(STOPWORDS)

for word in new_file.CONTENT: 
    word = str(word)
    tokens = words.split()

    for i in range(len(tokens)):
        tokens[i] = tokens[i].upper()

    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width = 1000, height = 1000, background_color ='white', stopwords = stopwords, min_font_size = 12).generate(comment_words)

plot.figure(figsize = (8,8), facecolor = None)
plot.imshow(wordcloud)
plot.axis("off")
plot.tight_layout(pad = 0)

plot.show

