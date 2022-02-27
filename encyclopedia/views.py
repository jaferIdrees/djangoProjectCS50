from django.shortcuts import render
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def explore(request, title):
    if util.get_entry(title) != None:
       return render(request, "encyclopedia/title.html", {
        "title":title,
        "page": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/title.html", {
            "title":title,
        "page": "Title not found"
         })
        
    
