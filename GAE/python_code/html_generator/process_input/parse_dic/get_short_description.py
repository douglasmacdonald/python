# -*- coding: utf-8 -*-

#from kitchen.text.converters import to_unicode

from set_basket_list import set_basket_list

def get_short_description(html_page_get_multi_dic, performance_id_dic):

    basket_list = set_basket_list(html_page_get_multi_dic, performance_id_dic)

    short_description = ""
    for item in basket_list:

        short_description = short_description \
            + unicode(item['number_of_item'])\
            + u"x"\
            + item['item_description']\
            + u"@£" + item['price'] + ""\
            + u" = £" + item['cost'] + ". "

    return short_description
