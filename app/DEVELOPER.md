<h1>Documentação</h1>

## data.config
Tem o banner do projeto + informações do autor.

## downloader.py
Tem como papel retornar a versão atual do google-chrome para facilitar na hora do usuário final for fazer o download.

## scrape_links.py
Recebe um código html e vai filtrando até conseguir retornar todos os links de vídeos.

## source_code.py
Pega o código html da página alvo do tiktok e retorna o código. Nesse caso usamos o selenium pois o tiktok tem um sistema robusto de identificação de bots e automações 
e acaba impedindo com metódos mais simples como um requests por exemplo.
