from no_brainer import HTMLGenerator
from no_brainer import (
    _generate_common_component,
    _generate_div_component,
    _generate_href_component,
    _generate_span_component,
)

HTMLGenerator.generate_component(component_type)


generator_functions = {
    "common": generate_common_component,
    "href": generate_href_component,
    "span": generate_span_component,
    "div": generate_div_component,
}

generator_functions[component_type]()
