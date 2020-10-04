# -*- coding: utf-8 -*-
# Demo only - please don't use in production

import scrapy
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
import os
 
class QuotesSpider(Spider):
    name = 'quotes'
    start_urls = ['https://www.lse.co.uk/login.html']

    def parse(self, response):
        yield FormRequest(url=self.start_urls[0],
                                         formdata={
                                        'txtEmail': os.environ.get('txtEmail'),
                                        'txtPassword': os.environ.get('txtPassword'),
                                        'txtFormType': 'LOGIN',
                                        'txtLoginSOurce':'NAV',
                                        'g-recaptcha-response-v3' : '03AGdBq25zeWpXxGw1re98OsKP8lHUUDSI0MxqYX_aqxbgJl0_p8YyjsRr8JRc9bKAspCvBh0HYvnMyEJss2UvvLp55vb8Vkkhg9zN56xGPcJjXQiq1MWuLERlShqQVi820neJ0UFF5Sx63woVGtay_vDrJSnHPpHWDqyJu9q8b_EUksy6kBKvgoUERB67rdaNdUwRu2k0gjT_mhLImnLWGt085xFe4tEguYj-XVG2gUV-Df3rXnttI1ygquOrUeO4uF6WPhcvW6Ml6OUucNj9IDeyDtf-EuAEmiWMjdusiARVTj_3pyIjDC23EZueKioVMMLd7Gi2P0J_I87ivimFKn3gZpeIk8Yt3l7jr3qr1n8Mhe1CuPwDHpgu145y9mXi-xUCeJF-tKTshAwRs_XGNfnw-japfS8fh_UNv-sJA-yf1QjbwQlSC7w'
                                                   },
                                         callback=self.scrape_ftse100_page)
 
    def scrape_ftse100_page(self, response):
        print("logged in!")
        # do stuff / go to next page
        url = 'https://www.lse.co.uk/share-prices/indices/ftse-100/'
        yield scrapy.Request(url=url, callback=self.parse_100)

    def parse_100(self,response):
        open_in_browser(response)
 
