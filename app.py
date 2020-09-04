
from flask import Flask, request, render_template
import os.path
import os

IMG_PER_PAGE = 10
IMG_SUFFIX = [".jpg","jpeg",".gif",".svg",".png"]

def img_filter(file):
    for sfx in IMG_SUFFIX:
        if file.endswith(sfx) :
            return True
    return False

def list_file():
    return list(map(lambda name : "assets/" + name,  filter(img_filter, os.listdir("assets"))))

def compose(content, page, per_page):
    pages = (len(content) + per_page - 1) // per_page
    return {
        "page" : page,
        "pages" : pages,
        "items" : content[per_page * page: per_page * page + per_page],
        "has_next" : page < pages -1,
        "has_prev" : page > 0,
        "next" : page + 1,
        "prev" : page -1
    }

app = Flask(__name__,
    static_url_path='/assets',
    static_folder='assets'
)

@app.route("/")
def render_page():
    page = int(request.args.get('page', 0));
    per_page = int(request.args.get('per_page', IMG_PER_PAGE));
    content = list_file()
    print(content)

    return render_template("template.html", data = compose(content, page, per_page))

if __name__ == "__main__" :
    app.run(host='0.0.0.0')