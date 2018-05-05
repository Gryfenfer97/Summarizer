# -*- coding: utf-8 -*-

from kadotdev.models import summarizer
import sys
import os


def create_list(lang):
    liste = []
    i=0
    listText = os.listdir("texts/{}/".format(lang))
    while i<=len(listText) - 1:
        my_file = open("texts/{}/{}".format(lang,str(listText[i])),"r")
        liste.append(my_file.read())
        my_file.close()
        i+=1

    return liste

def summarize(path,sentence_number,lang):

    my_file = open(path,"r")
    to_summarize = my_file.read()
    my_file.close()

    liste = create_list(lang)
    summary = summarizer(to_summarize,liste,sentence_number,topic_threshold=0.002)

    return summary
if __name__ == '__main__':
    path = str(sys.argv[1])
    sentence_number = int(sys.argv[2])
    lang = str(sys.argv[3])
    arg4 = str(sys.argv[4])

    if (arg4 == '-o'):
        file_name = path.split('/')[len(path.split('/'))-1].split('.')[0]
        summary = summarize(path,sentence_number,lang)
        output_path = str(sys.argv[5])
        output_html = '<h1>Résumé du du fichier {}</h1>\n<p>{}</p>'.format(file_name,summary)
        my_file = open(output_path,'w')
        my_file.write(output_html)
        my_file.close()
