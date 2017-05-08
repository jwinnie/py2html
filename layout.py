def split_half(left, right, divider_position=(6)):
    
    return """<div class="row"><div class="col-sm-{}">{}</div><div class="col-sm-6">{}</div></div>""".format(divider_position, left, 12-divider_position, right)
    
def split_thirds(left, middle, right, divider_position=(4,4)):
    
    return """<div class="row"><div class="col-sm-{}">{}</div><div class="col-sm-{}">{}</div><div class="col-sm-{}">{}</div></div>""".format(divider_position[0], left, divider_position[1], middle, 12-divider_position[0]-divider_position[1], right)
