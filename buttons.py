def btn(content, onclick, size=""):
    
    return """<button class="btn btn-primary btn-{}" onclick="{}">{}</button>""".format(size, onclick, content)
    
def btn_secondary(content, onclick, size=""):
    
    return """<button class="btn btn-secondary btn-{}" onclick="{}">{}</button>""".format(size, onclick, content)
    
def btn_green(content, onclick, size=""):
    
    return """<button class="btn btn-success btn-{}" onclick="{}">{}</button>""".format(size, onclick, content)
    
def btn_red(content, onclick, size=""):
    
    return """<button class="btn btn-danger btn-{}" onclick="{}">{}</button>""".format(size, onclick, content)
    
def btn_yellow(content, onclick, size=""):
    
    return """<button class="btn btn-warning btn-{}" onclick="{}">{}</button>""".format(size, onclick, content)
    
def btn_light_blue(content, onclick, size=""):
    
    return """<button class="btn btn-info btn-{}" onclick="{}">{}</button>""".format(size, onclick, content)
    
def onclick_link(url, is_newtab=False):
    
    return "window.location='{}';".format(url) if not is_newtab else "window.open('{}', '_blank')".format(url)
        
def onclick_submit(form_id):
    
    return "document.getElementById('{}').submit();".format(form_id)
