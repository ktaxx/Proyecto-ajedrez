
piezas = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
}


def validar_fen(fen):
    partes = fen.split()

    if len(partes) != 6:
        print("Error: la cadena FEN no tiene las 6 partes necesarias.")
        return False

    filas = partes[0].split('/')
    if len(filas) != 8:
        print("Error: deben existir exactamente 8 filas separadas por '/'.")
        return False

    reyes_blancos = 0
    reyes_negros = 0

    for i, fila in enumerate(filas, start=1):
        conteo = 0
        for c in fila:
            if c.isdigit():
                conteo += int(c)
            elif c in piezas:
                conteo += 1
                if c == 'K': 
                    reyes_blancos += 1
                elif c == 'k': 
                    reyes_negros += 1
            else:
                print(f"Error: carácter inválido '{c}' en la fila {i}.")
                return False

        if conteo != 8:
            print(f"Error: la fila {i} tiene {conteo} casillas (debe tener 8).")
            return False

    if reyes_blancos != 1 or reyes_negros != 1:
        print("Error: debe haber exactamente un rey blanco y un rey negro.")
        return False

    if partes[1] not in ['w', 'b']:
        print("Error: el turno debe ser 'w' (blancas) o 'b' (negras).")
        return False

    enroque = partes[2]
    for c in enroque:
        if c not in "KQkq-":
            print("Error: el campo de enroque contiene caracteres inválidos.")
            return False

    en_passant = partes[3]
    if en_passant != "-":
        columna = en_passant[0]
        fila = en_passant[1]
        if len(en_passant) != 2 or columna not in "abcdefgh" or fila not in "36":
            print("Error: el campo en passant no es valido(por ejemplo: e3 o e6)")
            return False

    if not partes[4].isdigit():
        print("Error: el campo de halfmove clock debe ser un número.")
        return False

    if not partes[5].isdigit() or int(partes[5]) < 1:
        print("Error: el campo de fullmove counter debe ser un número mayor o igual a 1.")
        return False

    return True


def convertir_tablero(fen):
    filas = fen.split()[0].split('/')
    tablero = []

    for fila in filas:
        fila_tablero = []
        for c in fila:
            if c.isdigit():
                fila_tablero += ['.'] * int(c)
            else:
                fila_tablero.append(piezas.get(c, '?'))
        tablero.append(fila_tablero)

    return tablero


def dibujar_tablero(tablero):
    print("\nTablero de ajedrez:")
    for fila in tablero:
        print(' '.join(fila))
    print()


def main():
    print("===========================================")
    print("      Analizador de cadenas FEN (Ajedrez)  ")
    print("===========================================\n")

    fen = input("Escribe una cadena FEN: ")

    if validar_fen(fen):
        print("\n La cadena FEN es válida.")
        tablero = convertir_tablero(fen)
        dibujar_tablero(tablero)
        print("Turno:", "Blancas" if fen.split()[1] == 'w' else "Negras")
        print("Enroque:", fen.split()[2])
        print("En passant:", fen.split()[3])
        print("Halfmove clock:", fen.split()[4])
        print("Fullmove counter:", fen.split()[5])
    else:
        print("\n la cadena de FEN es invalida.")


if __name__ == "__main__":
    main()
