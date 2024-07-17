import scrapy

class ApplyLeavePageSpider(scrapy.Spider):
    name = 'apply_leave_page_spider'

    def parse(self, response):
        selector = scrapy.Selector(text=response)

        # Extracting the filled data using XPath
        leave_type = selector.xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[@class="oxd-select-text-input"]/text()').get()
        from_date_value = selector.xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input/@value').get()
        to_date_value = selector.xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input/@value').get()
        comments_value = selector.xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/textarea/text()').get()

        print("Leave Type:", leave_type)
        print("From Date:", from_date_value)
        print("To Date:", to_date_value)
        print("Comments:", comments_value)


