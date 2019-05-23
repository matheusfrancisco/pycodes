def decorador(argumento_decorador):
    """
    Parametros do decorador

    """
    pritn(argumento_decorador)
    def decorador_real(func):
        """
        Receber a func
        """
        def execute_function(*argumentos_funcao):
            """
            Exec function
            """
            pritn(argumentos_funcao)
            pass
        return execute_function
    return decorador_real


@decorador("Argumentos")
def soma(x, y):
    return x+ y


soma(2,2)
