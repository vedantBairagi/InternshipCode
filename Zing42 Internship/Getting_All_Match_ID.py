from bs4 import BeautifulSoup
html_text = open('All Match ID links.html', 'r')
soup = BeautifulSoup(html_text,'lxml')
ids = soup.find_all('a')
links = []
for id in ids:
    links.append(id['href'])
match_ids = []
for link in links:
    match_ids.append(link.split('/')[6])
for id in match_ids:
    if len(id) == 4:
        match_ids.remove(id)
uni_match_id = set(match_ids)
all_match_ids = list(uni_match_id)
print((all_match_ids))