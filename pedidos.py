import conexion

#Duma Roberto Zelaya Mejia 
#Roberto Carlos Hernandez Melendez
#Jose Roberto Del Rio Maravilla

db = conexion.conexion()


class pedidos:
    def consultar_pedidos(self):
        sql = "SELECT * FROM pedidos"
        return db.consultar(sql)

    def administrar_pedidos(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO pedidos (id_usuarios, id_res, img_url, nombre, descripcion, precio) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (contenido["id_usuarios"], contenido["id_res"], contenido["img_url"], contenido["nombre"], contenido["descripcion"], contenido["precio"])

            elif contenido["accion"]=="modificar":
                sql = "UPDATE usuario SET nombre=%s, apellido=%s, correo=%s, contra=%s, direccion=%s WHERE id_usuarios=%s"
                val = (contenido["nombre"], contenido["apellido"], contenido["correo"], contenido["contra"], contenido["direccion"], contenido["id_usuarios"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM alumnos WHERE idAlumno=%s"
                val = (contenido["idAlumno"],)

            return db.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)