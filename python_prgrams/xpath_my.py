#!/usr/bin/python
import libxml2
import re

def xpath(document,search):

        doc = libxml2.parseFile(document)
        for url,name in zip(doc.xpathEval('//category//categoryPageURL//text()'), doc.xpathEval('//category//name//text()')) :

         if url.content == search:
          name_url = "filename::"+ document + " Category Name::"+ name.content+ "       Category url::"  + url.content
          print name_url
