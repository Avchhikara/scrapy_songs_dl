import scrapy

from ..items import Song

class SongSpider(scrapy.Spider):
    name = "song"
    visited = set()
    def start_requests(self):
        targets = [
            "https://djpunjab.fm/",
            # "https://www.pendujatt.net/punjabi-songs.html"
        ]
        for target in targets:
            yield scrapy.Request(target, callback=self.parse)

    def parse(self, response, depth=1000):
        if depth>0:
            links = response.xpath('//a')
            next_links = []
            self.visited.add(response.url)
            for link in links:
                url = link.xpath('@href').extract()[0]
                text = link.xpath('text()').extract()[0]
                if url.endswith('.mp3') and "320" in text:
                    yield Song(text=text, url=url)
                else:
                    next_links.append(url)
                
            for next_link in next_links:
                if next_link not in self.visited:
                    yield scrapy.Request(next_link, callback=lambda *x: self.parse_hof(*x, depth=depth - 1))

    def parse_hof(self, *args, depth):
        return self.parse(*args, depth=depth)
