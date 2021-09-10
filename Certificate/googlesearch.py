from googlesearch import search


class GoogleSearch:
    def __init__(self, search_query):
        self.query = search_query
        for i in search(query=self.query, tld='co.in', lang='en', num=15):
            print(i + '\n')


if __name__ == '__main__':
    output = GoogleSearch(input('Google Search Here:'))
    print(output)