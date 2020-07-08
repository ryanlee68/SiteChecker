import requests

class SiteChecker:

    # websites is a string list of the websites you want to check (remember to include https://)
    def __init__(self, websites):
        self.websites = websites

    # checks if there are broken links in the websites variable, if there are broken website(s), then it returns a list of the broken website(s)
    def checkSites(self):
        broken_links = []
        for website in self.websites:
            try:
                if not website.startswith('https://'):
                    return f'ERROR: {website} has to start with https://'
                requeststat = requests.get(website).status_code
                if requeststat == 404 or requeststat == 403:
                    broken_links.append(website)
            except:
                broken_links.append(website)
        try:
            if len(broken_links) != 0:
                print('There are broken links')
                return broken_links
            else:
                return 'There are no broken links'
        except ConnectionRefusedError as error:
            print('There are broken links')
            return broken_links

# the lines of code are an example, https://oaisbndfoianfiopaw.com is a broken link, so it should return a list of that website
jack = SiteChecker(['https://google.com', 'https://tesla.com', 'https://oaisbndfoianfiopaw.com'])
print(jack.checkSites())
