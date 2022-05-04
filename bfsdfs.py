import requests
from bs4 import BeautifulSoup
from collections import deque
def dfs(base, path, visited, max_depth=2, depth=0):
    if depth < max_depth:
        try:
            soup = BeautifulSoup(requests.get(base + path).text, "html.parser")

            for link in soup.find_all("a"):
                href = link.get("href")

                if href not in visited:
                    visited.add(href)
                    print(f"At Depth {depth}: {href}")

                    if href.startswith("http"):
                        dfs(href, "", visited, max_depth, depth + 1)
                    else:
                        dfs(base, href, visited, max_depth, depth + 1)
        except:
            pass
def bfs(base, path, visited,dq, max_depth=2, depth=0):
    while dq:
        base, path, depth = dq.popleft()
    
        if depth < max_depth:
            try:
                soup = BeautifulSoup(requests.get(base + path).text, "html.parser")
    
                for link in soup.find_all("a"):
                    href = link.get("href")
    
                    if href not in visited:
                        visited.add(href)
                        print("  " * depth + f"At Depth {depth}: {href}")
    
                        if href.startswith("http"):
                            dq.append([href, "", depth + 1])
                        else:
                            dq.append([base, href, depth + 1])
            except:
                pass
print('------------------------ Using Depth First Search ------------------------ ')    
dfs("https://animixplay.to/", "", set(["https://animixplay.to/"]))
print('------------------------ Using Breadth First Search ------------------------ ')
bfs("https://animixplay.to/", "", set(["https://animixplay.to/"]),deque([["https://animixplay.to/", "",
0]]))

