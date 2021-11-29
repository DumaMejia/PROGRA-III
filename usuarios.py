import conexion

db = conexion.conexion()


class usuarios:
    def consultar_usuarios(self):
        sql = "SELECT * FROM usuario"
        return db.consultar(sql)

    def administrar_usuarios(self, contenido):
        try:
            if contenido["accion"]=="nuevo":
                sql = "INSERT INTO usuario (nombre, apellido, correo, contra, direccion) VALUES (%s, %s, %s, %s, %s)"
                val = (contenido["nombre"], contenido["apellido"], contenido["correo"], contenido["contra"], contenido["direccion"])

            elif contenido["accion"]=="modificar":
                sql = "UPDATE alumnos SET codigo=%s, nombre=%s, telefono=%s WHERE idAlumno=%s"
                val = (contenido["codigo"], contenido["nombre"], contenido["telefono"], contenido["idAlumno"])

            elif contenido["accion"]=="eliminar":
                sql = "DELETE FROM alumnos WHERE idAlumno=%s"
                val = (contenido["idAlumno"],)

            return db.ejecutar_consulta(sql, val)
        except Exception as e:
            return str(e)