#Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#domain_name("http://github.com/carbonfive/raygun") == "github" 
#domain_name("http://www.zombie-bites.com") == "zombie-bites"
#domain_name("github.com") == "github"
def domain_name(url):
    try: url = url.split("//")[1].split(".")
    except: url = url.split(".")
    if url[0] == "www": return url[1]
    else: return url[0]
