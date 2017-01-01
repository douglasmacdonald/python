def process(handler_mapping, webapp_debug):
    """"""

    template_variables = {
        'list_of_handlers_and_pages' : handler_mapping
        , 'webapp_debug_true_or_false' : webapp_debug
    }

    return template_variables
