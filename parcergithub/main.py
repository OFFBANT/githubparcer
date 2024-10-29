import requests
from bs4 import BeautifulSoup
import click

link =  "https://github.com/"

@click.command()
@click.option("--rep", prompt='repository author/name', help='input repository in format author/repository')

def parcer(rep):
    responce = requests.get(f"{link}{rep}").text
    soup = BeautifulSoup(responce, 'lxml')
    block = soup.find('div', class_='hide-sm hide-md')
    check_stars = block.find_all('div', class_='mt-2')[3]
    res_stars = check_stars.find('strong').text

    click.echo(f"{res_stars} Stars")
    block_lang = soup.find('div', class_='BorderGrid about-margin')
    check_lang = block_lang.find_all('div', class_='BorderGrid-row')[5]
    lang_res = check_lang.find_all('span')[2].text

    click.echo(f"Languages: {lang_res}")
    responce_issues = requests.get(f"{link}{rep}/issues").text
    soup_issues = BeautifulSoup(responce_issues, 'lxml')
    block_issues = soup_issues.find('div', class_='table-list-header-toggle states flex-auto pl-0')
    issues = block_issues.find('a', class_='btn-link selected').text
    click.echo(f'Open issues: {issues}')


if __name__ == "__main__":
    parcer()
