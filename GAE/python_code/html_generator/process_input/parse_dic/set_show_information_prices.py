from configuration import product_id_dic as performance_id_dic
from get_performance_id import get_performance_id

def set_show_information_prices(multi_dict):

    performance_id = get_performance_id(multi_dict)

    performance_information = performance_id_dic.get(performance_id, {})

    performance_information_general_admission_price = \
        performance_id_dic.get(performance_id, {}).get(
            'admission_price', [{}])[0].get('price', "")
     
    performance_information_concession_admission_price = \
        performance_id_dic.get(performance_id, {}).get(
            'admission_price', [{}, {}])[1].get('price', "")

    performance_information_general_admission_face_value = \
        performance_id_dic.get(performance_id, {}).get(
            'admission_price', [{}])[0].get('general_admission_face_value', "")

    performance_information_concession_admission_face_value = \
        performance_id_dic.get(performance_id, {}).get(
            'admission_price', [{}, {}])[1].get(
                'concession_admission_face_value', "")

    return (performance_information
        , performance_information_general_admission_price
        , performance_information_concession_admission_price
        , performance_information_general_admission_face_value  
        , performance_information_concession_admission_face_value)

