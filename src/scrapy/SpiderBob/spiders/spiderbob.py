#!/usr/bin/env python3
"""
SpiderBob is a crawler that uses Scrapy to scrape
SpongeBob dialogue from transcripts that are hosted
on the SpongeBob wiki.

"""

import scrapy

class SpiderBob(scrapy.Spider):
    """
    SpiderBob class, scrapes SpongeBob dialogue
    """
    name = "SpiderBob"
    allowed_domains = ["spongebob.wikia.com"]
    start_urls = ["http://spongebob.wikia.com/wiki/List_of_transcripts"]

    def parse(self, response):
        """
        makes requests to urls that are present in the urlBook
        """
        urlBook = self.makeBook(response)
        for url in urlBook.values():
            yield scrapy.Request(url, callback = self.parseTranscript)


    def parseTranscript(self, response):
        """
        parses a transcript page and any dialogue of SpongeBob
        is converted to string to be appeneded to data file
        """
        dialogue = response.css("#mw-content-text ul li")
        f = open("../../data/spongeTranscript.txt", "a+")
        for text in dialogue:
            if text.css("b::text").extract()[0] == "SpongeBob:":
                lines = text.css("li::text").extract()
                for x in lines:
                    line = str(x)
                    line.strip()
                    f.write(line)
        f.close()


    def makeBook(self, response):
        """
        parses first page and compiles a dictionary of urls and returns it
        """
        links = {}
        for i,link in enumerate(response.css(".wikitable a::attr(href)").extract()):
            end = str(link)
            end = end[5:]
            print(end)
            if end[-10:] != "transcript":
                continue
            else:
                nextPage = "http://spongebob.wikia.com/wiki" + end
                links[i] = nextPage

        return links

