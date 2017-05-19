# coding=utf-8
import os
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"

soup = BeautifulSoup(html_doc, 'html.parser')

import re

def has_class_but_no_id(tag):
    boa = tag.has_attr('class');
    bob = tag.has_attr('id')
    # print boa
    # print bob
    return boa and not bob

tag = soup.find('a')
# print has_class_but_no_id(tag)
# print dir(os)
# print os.getcwd()

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fibo')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')
# print d.tricks
# print e.tricks

import re
str3 = 'imooc video = 999'
# print str3
def add1(match):
    val = match.group()
    num = int(val) + 1
    return str(num)

str3 = re.sub(r'\d+', add1, str3)
# print str3

str4 = 'imooc:C C++ Java Python,C#'

lst = re.split(r':| |,', str4)

print lst[-1]

# for tag in soup.find_all(True):
#     print(tag.name)

# for tag in soup.find_all(re.compile('t')):
#     print(tag.name)
#
# print soup.find_all(['a', 'b'])

# links = soup.find_all('a')
# for link in links:
#     print link.get('href')
# last_a_tag = soup.find('a', id='link3')
# print last_a_tag
# print last_a_tag.previous_element.next_element
# print last_a_tag.next_element.next_element.next_element.next_element
# print last_a_tag.next_sibling.previous_sibling
# for sibling in soup.a.next_siblings:
#     print(repr(sibling))
# link = soup.a
# print list(soup.a.next_siblings)
# print link
# print link.next_sibling.next_sibling

# for link in soup.find_all('a'):
#     print link.get('href')



#
# title_tag = soup.title
#
# html_tag = soup.html
# print html_tag

# print title_tag
# print title_tag.parent
# print title_tag.string.parent

# for string in soup.strings:
#     print (repr(string))

#print(soup.prettify())

# print soup.title

# print len(soup.find_all('a'))

# for childNode in soup.descendants:
#     print str(childNode) + "\n"

# for link in soup.find_all('a'):
#      print(link.get('href'))


# soup = BeautifulSoup(markup, 'html.parser')
# comment = soup.b.string
# print type(comment)
# print comment
# print(soup.b.prettify)



# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
# print(sibling_soup.prettify())
# print sibling_soup.c.previous_sibling
# print sibling_soup.b.next_sibling
# print sibling_soup.b.string