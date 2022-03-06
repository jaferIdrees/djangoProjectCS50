
from turtle import title
from django.shortcuts import render
from . import util
import random
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def new_entry(request):
    if request.method =="POST":
        title = request.POST["title"]
        text = request.POST["body_text"]
        if util.list_entries().__contains__(title):
            return render(request, "encyclopedia/title.html", {
            "title":title,
        "page": "The page already exists"
         })
        util.save_entry(title,"#"+title+"\n"+text)
        return explore(request, title)
    return render(request, "encyclopedia/new_entry.html")

def edit_page(request, name):
    title = name
    return render(request, "encyclopedia/edit_entry.html", {
        "title":title,
        "page": util.get_entry(title)
        })

def save_page(request):
    if request.method =="POST":
        title = request.POST["title"]
        text = "#"+title+"\n"+request.POST["body"]
        util.save_entry(title, text)
        return explore(request, title)
    

def explore(request, title):
    if util.get_entry(title) != None:
       return render(request, "encyclopedia/title.html", {
        "title":"",
        "page": markdown.markdown(util.get_entry(title))
        })
    else:
        return render(request, "encyclopedia/title.html", {
            "title":title,
        "page": "Title not found"
         })
def random_page(request):
    title = random.choice(util.list_entries())
    return render(request, "encyclopedia/title.html", {
        "title":"",
        "page": util.get_entry(title)
        })
    
def search(request):
    q_text = request.POST['q']
    matches = []
    if util.list_entries().__contains__(q_text):
      return explore(request, q_text)
    else:
      for entry in util.list_entries():
          ent = entry.lower()
          if ent.__contains__(q_text.lower()): matches.append(entry)
      return render(request, "encyclopedia/index.html", {
        "entries": matches
    })
   