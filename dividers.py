def separator():
    
    return "<hr/>"
    
def banner(content):
    
    return """<div class="jumbotron">{}</div>""".format(content)
    
def br(lines=1):
    
    output = ""
    for _ in range(lines):
        output += "<br/>"
    
    return output
