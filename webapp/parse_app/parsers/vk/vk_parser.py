import json
import datetime
import vk


class Parser:
    def __init__(self, api):
        self.api = api

    def get_news_from_tag(self, hashtag, count=0):
        """
          hashtag - хештег новости
          count - количество первых записей для вывода * 200
        """
        
        data = []
        for i in range(count):
            request = self.api.newsfeed.search(q=hashtag,
                                               v='5.130',
                                               count=200,
                                               start_from=i)
            data += [self.parse_item_to_dict(item)
                      for item in request['items']]
        
        return data

    def parse_item_to_dict(self, data):
        item = {}
        item['id'] = data['id']
        item['text'] = data['text']
        item['review_quantity'] = None
        item['stars'] = None
        item['date'] = None
        item['date_create'] = self.unix_to_date(data['date'])
        item['order_type'] = None
        item['place'] = "ostankino_tower"
        item['translated'] = None
        item['converted_date'] = self.unix_to_date(data['date'])

        return item

    def unix_to_date(self, unix_date):
        date = datetime.datetime.fromtimestamp(unix_date)

        return date.strftime('%d.%m.%Y %H:%M')
    
def get_json_file(data):
    with open('data.json', 'w') as fp:
      json.dump(data, fp, ensure_ascii=False)
      