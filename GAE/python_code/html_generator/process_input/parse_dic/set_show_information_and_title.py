from configuration import show_information as shows_information_dic
from get_show_id import get_show_id

def set_show_information_and_title(multi_dic):

    show_id = get_show_id(multi_dic);

    return (
        shows_information_dic.get(
                show_id, {'show_description':"No known show selected"})

        , shows_information_dic.get(
            show_id, {'title':"No show selected."})['title']
        )


