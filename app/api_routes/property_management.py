from . import api


@api.route('/property/index')
def p_index():
    return 'property index'
