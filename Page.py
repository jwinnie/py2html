class Page:
    
    def __init__(self, title=""):
        
        self.contents_string = ""
        self.name = title
        
    def generate(self):
    
        generated_text = ""
        
        with open("page_template.html") as template:
            # Skip to line 5 because of comments in beginning of file
            for i in range(5):
                template.next()
            for line in template:
                generated_text += line
        
        # Remove newlines, spaces, etc and replace {} with values
        return "".join(.split(generated_text)).format(self.name, self.contents_string)
