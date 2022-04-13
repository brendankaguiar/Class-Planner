import scrapy

class CourseSpider(scrapy.Spider):
    name = "courses"
    start_urls = ['https://catalog.unr.edu/preview_degree_planner.php?catoid=24&poid=17619']

    def parse(self, response):
        n = 0
        for course in response.css('td.course::text').getall():
            yield {
                n : course
            }
            n = n + 1
                    