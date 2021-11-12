import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import wikipedia
import re


wiki = wikipedia.page('Gilgit-Baltistan') # Extract the plain text content of the pagei
text = wiki.content 
text = re.sub(r'==.*?==+', '', text) #adding the contents to a variable, and making it legible for wordcloud module
text = text.replace('\n', '')

def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30)) # input cloud size
    plt.imshow(wordcloud) #display wordcloud
    plt.axis("off"); # no axis details


#defining the wordclouds total width, height, colors
wordcloud = WordCloud(width= 3000, height = 2000, random_state=1, background_color='green', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)# Plot
plot_cloud(wordcloud)

# Save image
wordcloud.to_file("wordcloud.png")
