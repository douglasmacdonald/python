from process_index_page import process

def get_index_page_html(
    html_template_render
    , handler_mapping
    , webapp_debug
    , logger):

    logger.info("Funciton: get_index_page_html")
    template_variables = process(handler_mapping, webapp_debug)

    return html_template_render(template_variables)
