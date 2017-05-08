def form(content, action, secure, form_id):
    
    return """<form method="{}" action="{}" id="{}">{}</form>""".format("post" if secure else "get", action, form_id, content)
    
def inline_form(content, action, secure, form_id):
    
    return """<form class="form-inline" method="{}" action="{}" id="{}">{}</form>""".format("post" if secure else "get", action, form_id, content)  

def form_group(header, content):
    
    return """<fieldset class="form-group"><legend>{}</legend>{}</fieldset>""".format(header, content)
    
def input_text(input_type, name, placeholder):
    
    return """<input type="{}" class="form-control" name="{}" id="{}" placeholder="{}"/>""".format(input_type, name, name, placeholder)
    
def input_text_warning(input_type, name, placeholder, feedback=""):
    
    return """<span class="has-warning"><input type="{}" class="form-control form-control-warning" name="{}" id="{}" placeholder="{}"/><div class="form-control-feedback">{}</div></span>""".format(input_type, name, name, placeholder, feedback)
    
def input_text_danger(input_type, name, placeholder, feedback=""):
    
    return """<span class="has-danger"><input type="{}" class="form-control form-control-danger" name="{}" id="{}" placeholder="{}"/><div class="form-control-feedback">{}</div></span>""".format(input_type, name, name, placeholder, feedback)
    
def input_text_success(input_type, name, placeholder, feedback=""):
    
    return """<span class="has-success"><input type="{}" class="form-control form-control-success" name="{}" id="{}" placeholder="{}"/><div class="form-control-feedback">{}</div></span>""".format(input_type, name, name, placeholder, feedback)
    
def input_selector(name, options):
    
    options_html = ""
    
    for option in options:
        
        options_html += "<option>{}</option>".format(option)
    
    return """<select class="form-control" name="{}">{}</select>""".format(name, options_html)
    
def input_textarea(name, rows):
    
    return """<textarea name="{}" rows="{}"/>""".format(name, rows)
    
def input_checkbox(name, content):
    
    return """<div class="form-check"><label class="form-check-label"><input type="checkbox" class="form-check-input" name="{}">{}</label></div>""".format(name, content)
    
def input_file(name):
    
    return """<input type="file" class="form-control-file" name="{}">""".format(name)
    
def form_label(content, input_name):
    
    return """<label for="{}">{}</label>""".format(input_name, content)
    
def form_description(content):
    
    return """<small class="form-text text-muted">{}</small>""".format(content)
