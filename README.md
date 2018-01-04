# xy-inc
Teste admissional para Zup

Instruções de instalação:

	1. Instalar Python 3 na máquina do servidor;  
	2. Atualizar pip com *python -m pip install -U pip* no Windows e pip install -U pip em outras plataformas;  
	3. Instalar Django com *python -m pip install django* no Windows e *pip install django* em outras plataformas;
	4. Instalar Django Rest Framework com *python -m pip install djangorestframework* no Windows e *pip install djangorestframework* em outras plataformas;
	5. Navegar até a pasta xy_inc e executar o comando *python manage.py runserver* para rodar a aplicação em localhost na porta 8000  
	
Instruções para teste manual:  

	O endpoint http://domínio:porta/POIs/ pode ser usado para listar todos os POIs cadastrados se chamado com o método GET e para cadastrar um POI se usado com o metódo POST com um JSON de acordo com o seguinte exemplo:  
		{  
			"nome": "Trabalho",  
			"coord_x": 35,  
			"coord_y": 5  
		}  

		
	O endpoint http://domínio:porta/POIs/{coordenada X}/{coordenada Y}/{d-max}/ pode ser usado para listar POIs por proximidade. Segue um exemplo de URL:  
		http://127.0.0.1:8000/POIs/20/10/10/