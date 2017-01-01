from configuration import performance_dic as performance_information_dic
from get_show_id import get_show_id

def set_show_times(html_page_get_multi_dic):

    show_id = get_show_id(html_page_get_multi_dic)

    return performance_information_dic.get(show_id, {})
