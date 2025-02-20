import markitdown
import re
import tempfile
import trafilatura
from bs4 import BeautifulSoup, Comment

_MEANINGLESS_TAGS = [
    'applet', 'audio', 'canvas', 'code', 'comment', 'datalist', 'embed',
    'figure', 'form', 'frame',
    'frameset', 'iframe', 'img', 'kbd', 'map', 'menu', 'noembed', 'noframes',
    'noscript', 'object', 'output',
    'plaintext', 'pre', 'ruby', 'samp', 'script', 'style', 'svg', 'title',
    'var', 'video', 'xmp'
]

_BLOCKLEVEL_TAGS = [
    'address', 'article', 'aside', 'blockquote', 'center', 'dd', 'details',
    'dialog', 'dir', 'div', 'dl', 'dt',
    'fieldset', 'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3',
    'h4', 'h5', 'h6', 'header', 'hgroup', 'hr',
    'isindex', 'li', 'main', 'menu', 'nav', 'noframes', 'noscript', 'ol', 'p',
    'pre', 'section', 'table', 'td', 'th',
    'tr', 'ul'
]


def html_to_article(html, format='html'):
    extract_kwargs = {
        'filecontent': html,
        'favor_recall': True,
        'output_format': 'html' if 'markdown' == format else format
    }
    article = trafilatura.extract(**extract_kwargs)

    if 'markdown' == format:
        article = re.sub(r'<cell>\s*<p>(.+?)</p>\s*</cell>', r'<td>\1</td>', article, flags=re.I | re.S)
        article = re.sub(r'<row[^>]*>(.+?)<\/row>', r'<tr>\1</tr>', article, flags=re.I | re.S)

        with tempfile.NamedTemporaryFile('w+t', suffix=".html") as f:
            f.write(article)
            f.flush()
            article = markitdown.MarkItDown().convert(f.name).text_content

        article = article.replace('\n```\n\n```\n', '\n```\n')

    return article


def fragment_to_text(html):
    if not len(html.strip()):
        return ''

    soup = BeautifulSoup(html, 'html.parser')
    if soup is None:
        raise ValueError('Can\'t build DOM tree with LXML')

    # Drop comments
    for comment in soup(string=lambda txt: isinstance(txt, Comment)):
        comment.extract()

    # Drop non-meaning tags
    for node in soup(_MEANINGLESS_TAGS):
        node.replace_with(soup.new_tag('br'))

    # Insert linebreaks around block-level tags
    for node in soup(_BLOCKLEVEL_TAGS):
        node.insert_before(soup.new_tag('br'))
        node.insert_before(soup.new_tag('br'))
        node.insert_after(soup.new_tag('br'))
        node.insert_after(soup.new_tag('br'))

    # Remove linebreaks inside text nodes (as browser does)
    for node in soup(string=lambda string: '\n' in string):
        node.string.replace_with(node.string.replace('\n', ' '))

    # Swap html linebreaks to normal ones
    for node in soup('br'):
        node.replace_with('\n')

    # Cleanup final text
    text = soup.getText()
    text = str(text).strip()
    text = re.sub(' {2,}', ' ', text)
    text = text.replace(' \n', '\n').replace('\n ', '\n')
    text = re.sub('\n{3,}', '\n\n', text)

    return text
