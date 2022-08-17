import arxiv
import json

with open("stopwords.txt", 'r') as sw:
    stopwords = sw.read().splitlines()

def get_first_author_surname(authors):
    return authors[0].name.split()[-1].lower()

def get_title_first_word(title):
    title = title.lower()
    for word in title.strip().split():
        if word not in stopwords:
            return word
    

def create_file(info):
    year = info.published.year if info.published.year else ""
    summary = info.summary if info.summary else ""
    arxiv_link = info.links[0].href if info.links[0].href else ""
    authors = ", ".join([a.name for a in info.authors])
    conference = info.journal_ref if info.journal_ref else ""
    
    with open(f"_publications/{get_first_author_surname(info.authors)}{year}{get_title_first_word(info.title)}.markdown", "w") as f:
        f.write("---\n")
        f.write("layout: publication\n")
        f.write(f"title: \"{info.title}\"\n")
        f.write(f"authors: {authors}\n")
        f.write(f"conference: {conference}\n")
        f.write(f"year: {year}\n")
        f.write(f"additional_links: \n\t- {{name: \"ArXiv\", url: \"{arxiv_link}\"}}\n")
        f.write(f"tags: [""]\n")
        f.write("---\n")
        f.write(summary)

def search_paper(name):
    search = arxiv.Search(
        query = "ti:"+name,
        max_results = 10,
        sort_by = arxiv.SortCriterion.Relevance
    )

    for result in search.results():
        correct = input(f"{result.title}, {result.authors[0]} \n[y/n]?\n")
        if correct == 'y':
            create_file(result)
        elif correct == 'q':
            break



adding = True
while(adding):
    paper_name = str(input("Input the paper title..\n")).strip()
    search_paper(paper_name)
    a = str(input("Do you want to add new paper? [y/n]"))
    if (a == "y"):
        adding = True
    else:
        adding = False

