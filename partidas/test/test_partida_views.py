from django.test import TestCase
from partidas.models import Partida
from partidas.models import Capitulo
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self,
              clave=2110,
              nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
              descripcion='Plumas, borradores, entre otras cosas.'
              ):

        self.admin_login()

        self.capitulo = Capitulo.objects.create(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

        self.partida = Partida.objects.create(
            clave=clave,
            nombre=nombre,
            descripcion=descripcion,
            capitulo=self.capitulo
        )

        self.data = {
            'clave': clave,
            'nombre': nombre,
            'descripcion': descripcion,
            'capitulo': self.capitulo
        }

    def test_crear_partida(self):
        respuesta = self.client.get('/partidas/nueva/')
        self.assertEqual(respuesta.status_code, 200)

    def test_template_correcto_nueva_partida(self):
        respuesta = self.client.get('/partidas/nueva/')
        self.assertTemplateUsed(respuesta, 'nueva_partida.html')

    def test_titulo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/partidas/nueva/')
        titulo = '<title>Nueva Partida</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    # def test_redireccion_al_agregar_partida(self):
    #     respuesta = self.client.post('/partidas/nueva/',
    # data=self.data)
    #     self.assertEqual(respuesta.url,'/partidas/lista/')

    # def test_redireccion_al_modificar_partida(self):
    #     self.agrega_partida()
    #     self.data['nombre'] = 'MATERIALES, ÚTILES
    #   Y EQUIPOS MENORES DE OFICINA2'
    #     respuesta = self.client.post('/partidas/editar/2110',
    # data=self.data)
    #     self.assertEqual(respuesta.url, '/partidas/lista/')

    def test_redireccion_al_eliminar_partida(self):
        respuesta = self.client.get('/partidas/eliminar/2110')
        self.assertEqual(respuesta.url, '/partidas/lista/')

    def test_lista_partidas(self):
        respuesta = self.client.get('/partidas/lista/')
        self.assertEqual(respuesta.status_code, 200)

    def test_materiales_se_encuentre_en_el_template(self):
        respuesta = self.client.get('/partidas/lista/')
        self.assertContains(respuesta, 'MATERIALES Y SUMINISTROS')

    def test_titulo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/partidas/nueva/')
        formulario = '<h1>Nueva Partida</h1>'
        self.assertInHTML(formulario, str(respuesta.content))

    def test_agregar_partida_form(self):
        id = Partida.objects.first().clave
        data = {
            'clave': 2110,
            'nombre': 'MATERIALES, ÚTILES Y EQUIPOS MENORES \
                DE OFICINA',
            'descripcion': 'Plumas, borradores, entre otras \
                cosas.',
            'capitulo': Capitulo.objects.first()
        }
        self.client.post('/partidas/editar/'+str(id), data=data)
        self.assertEqual(
            Partida.objects.first().nombre,
            'MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA')

    def test_boton_agregar_partida_en_template(self):
        response = self.client.get('/partidas/nueva/')
        boton = '<button class="btn btn-success" type="submit"> \
            Agregar</button>'
        self.assertInHTML(boton, str(response.content))

    def admin_login(self):
        user1 = User.objects.create_user(
            username='admin',
            password='Adri4na203#',
            is_superuser=True
        )
        self.client.login(username='admin', password='Adri4na203#')

    def agrega_capitulo(self):
        self.capitulo = Capitulo.objects.create(
            clave=3000,
            nombre='MATERIALES Y SUMINISTROS'
        )

    def agrega_partida(self):
        self.partida = Partida.objects.create(
            clave=3110,
            nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
            descripcion='Plumas, borradores, entre otras cosas.',
            capitulo=self.capitulo
        )
