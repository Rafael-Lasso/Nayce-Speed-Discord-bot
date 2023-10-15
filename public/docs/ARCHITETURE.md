
<div align="center">
    <img src="../assets/project/Avatar Nayce enchanted.png" width="200">
</div>

<br>

# Nayce Discord: Arqutetura

## Estrutura da Nayce


### Arquitetura


- Segue os preceitos da Clean Architeture

<div align="center">
    <img src="https://blog.cleancoder.com/uncle-bob/images/2012-08-13-the-clean-architecture/CleanArchitecture.jpg" width="350">
</div>

<div align="center">
    Fonte: <a style="color:#29f559; cursor:pointer;">https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html</a>
</div>


# 👩‍💻 Aplicação

Todos os Modulos da Aplicação, estão sendo englobados pelo package <b style="color: #1289DA;">core</b>

Representada pela pasta <b style="color: #FF6347;">App</b>
    

    Entities: Entidades encapsuladas ampla regras de negócios

Representada pela pasta <b style="color: #12C9F9;" >Commands</b>
    
    Use Cases: Encapsula e implementa todos os casos de uso do sistema


Representada pela pasta <b style="color: #b1b1b1;" >Manager</b>
    
    Interface Adapters: O software nesta camada é um conjunto de adaptadores que convertem dados do formato mais conveniente para os casos e entidades de uso, para o formato mais conveniente para alguma agência externa, como o banco de dados ou a Web


Representada pela pasta <b style="color: #FFD700;" >Services</b>
    
    Frameworks and Drivers: A camada mais externa é geralmente composta de estruturas e ferramentas como o banco de dados, o Web Framework etc. Geralmente você não escreve muito código nessa camada além do código de cola que se comunica com o próximo círculo para dentro.


<br>
