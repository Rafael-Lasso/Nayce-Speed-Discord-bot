<div align="center">
    <img src="./public/assets/project/Avatar Nayce enchanted.png" width="200">
</div>

## Nayce Discord

### Obejetivos da Nayce

<div>
    <ul>
        <li>Auxiliar na Moderação do Servidor</li>
        <li>Ser Simples de Usar e de se fazer manutenação</li>
        <li>Oferecer Recursos não disponiveis por outros Bots</li>
        <li>Ser Ultilizado tanto na Moderação de Servidores quanto por usuarios comuns </li>
    </ul>
</div>

### Não é um Obejetivos da Nayce

<div>
    <ul class="err-list">
        <li>Vencer Ronnie Coleman na quebra de braço</li>
    </ul>
</div>

## Estrutura da Nayce

* A Linguagem de desenvolvimento usada foi o <a href="https://www.python.org/">Python</a>, mas você pode optar por usar a Imagem dela no <a href="https://hub.docker.com/_/python">Docker Hub</a>

* Pasta public: acesso compartilhado e oferecem um jeito fácil e eficaz de coletar ( contem assets e documentações em arquivo .md )

* Pasta src: contem o Projeto em sua essencia

* Pasta test: Contem os testes da aplicação


<!-- <br> -->
## Ativar o Venv
O Projeto usa o Ambiente virtual Python para o Desenvolvimento

Para Criar rode o comando no terminal

Para ativar rode o comando no terminal

        python -m venv nome-do-ambiente-virtual


Windows

        cmd.exe: venv\Scripts\activate.bat
        PowerShell: venv\Scripts\Activate.ps1

POSIX

        PowerShell: venv/bin/Activate.ps1
        bash/zsh: source venv/bin/activate
        csh/tcsh: source venv/bin/activate.csh
        fish: source venv/bin/activate.fish

Depois Instale as Dependencias ultilizadas no projeto com o Comando

        pip install -r requirements.txt 