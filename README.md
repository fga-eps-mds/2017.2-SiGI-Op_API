<p align="center">
  <br>
    <a href="https://github.com/fga-gpp-mds/2017.2-SiGI-Op_API/wiki">
      <img src="https://github.com/fga-gpp-mds/2017.2-SiGI-Op_API/wiki/logo_gigacandanga.png" alt="GigaCandanga logo">
    </a>
</p>

<p align="center">

  [![Build Status](https://travis-ci.org/fga-gpp-mds/2017.2-SiGI-Op_API.svg?branch=master)](https://travis-ci.org/fga-gpp-mds/2017.2-SiGI-Op_API) [![Coverage Status](https://coveralls.io/repos/github/fga-gpp-mds/2017.2-SiGI-Op_API/badge.svg?branch=master)](https://coveralls.io/github/fga-gpp-mds/2017.2-SiGI-Op_API?branch=master) ![Python Version](https://img.shields.io/badge/python-3.5-blue.svg) ![Django Version](https://img.shields.io/badge/Django-1.11.4-green.svg) [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
</p>

Clique [aqui](https://sigi-op.herokuapp.com/) para acessar o SiGI-Op em produção

<br></br>
> API do projeto SiGI-Op - GigaCandanga


### O Que é a GigaCandanga
<p align=justify>
A GigaCandanga, rede metropolitana de educação e pesquisa, integra instituições de pesquisa e de ensino superior no Distrito Federal. É baseada numa infraestrutura de fibras ópticas própria, gerenciada em condomínio pelas instituições participantes. Começou a operar em 18 de dezembro de 2007, contando com a adesão até 2016 de 33 instituições.
</p>

### Qual Objetivo
<p align=justify>
O objetivo de promover a implantação de uma infraestrutura de fibras ópticas adequada à demanda de alta capacidade e atualização tecnológica, característica das instituições de pesquisa e de ensino superior.
</p>

### Como Funciona
<p align=justify>
A rede é baseada numa infraestrutura de fibras ópticas própria. Isto permite que as instituições de pesquisa e ensino superior explorem o potencial de conectividade em um patamar que não é oferecido pelos serviços comerciais. A capacidade mínima de qualquer conexão é de 1GB, podendo ser expandida facilmente conforme a demanda. Esta conectividade de alta capacidade permite que as instituições compartilhem aplicações e serviços inovadores, participando das redes acadêmicas avançadas, no país e no mundo. Por ser administrada na forma de consórcio, não só a capacidade é muito superior, como também os custos envolvidos são significativamente menores.
</p>

### O que será feito
<p align=justify>
O projeto Sistema de Gerenciamento de Infraestrutura (SiGI) consiste do desenvolvimento de uma aplicação com o objetivo de subsidiar a operação e a gestão da rede GigaCandanga.
</p>

## Configuração do ambiente

### Instalação

É utilizado o docker como forma de configuração de ambiente. Para utilizar o docker basta executar a seguinte linha de código:

Faça o download do Docker CE no [site oficial](https://docs.docker.com/engine/installation/).
Faça o download do Docker Compose no [site oficial](https://docs.docker.com/compose/install/).

Para construir novamente o container caso tenha feito alguma alteração no código utilize o seguinte comando

```
$ [sudo] docker-compose build
```

### Subindo o servidor

Para subir a aplicação no endereço `0.0.0.0` e na porta 8000 utilize o seguinte comando:

```
$ [sudo] docker-compose up
```

Acessar o endereço através de um Browser deve renderizar a API Django REST, como ilustrado abaixo:
![GitHub Logo](https://image.ibb.co/dVDokG/back.png)

Para visualizar o Fron End, acesse nosso [outro repositório](https://github.com/fga-gpp-mds/2017.2-SiGI-Op)

### Testes

Para executar todos os testes habilitados pelas flags contidas na lista `NOSE_ARGS` do arquivo `sigi_op/settings.py` basta executar:

```
$ [sudo] docker build -t my_env .
```

```
$ [sudo] docker run -it my_env python3 sigiop-API/manage.py test
```

Caso queira executar apenas os testes de um app específico:

```
$ [sudo] docker run -it my_env python3 sigiop-API/manage.py test app_name
```

### Folha de Estilo

Neste projeto é utilizado o padrão [PEP8](https://www.python.org/dev/peps/pep-0008/) e é utilizada a ferramenta [flake8](https://pypi.python.org/pypi/flake8) para verificar a folha de estilo. Para verificar todos os arquivos de código fonte `.py` deste projeto execute:

```
$ flake8
```

Caso queira verificar um app específico execute:

```
$ flake8 app_name
```

Também é utilizado neste projeto a ferramenta [pylint](https://www.pylint.org/) para análise estática de código em geral,
para executar a ferramenta siga os mesmos passos da flake8, tanto para executar utilizando todos os arquivos de código-fonte
do projeto como para um app específico, obviamente substituindo pelo comando `pylint`.

<p align="justify">
  <b>Acesse nosso repositório:</b>
    <a href="https://github.com/fga-gpp-mds/2017.2-SiGI-Op">Front End<br>
    </a>
</p>
