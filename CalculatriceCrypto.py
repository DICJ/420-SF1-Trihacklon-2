class CalculatriceCrypto:
    

    def puissance_10(n: int) -> int:
        """
        La plus grande puissance de 10 qui entre dans un nombre
        
            Examples: 
                puissance_10(567) = 100
                puissance_10(10) = 10
            
            Parameters:
                n (int): Un nombre
            
            Returns:
                La plus grande puissance de 10 qui entre dans un nombre
        """
        puissance = 0
        while n >= 10:
            n //= 10
            puissance += 1
        return 10 ** puissance

    def racine_carree(n: int) -> int:
        """
        Trouve le plancher de la racine carrée d'un nombre entier. Effectue une fouille dichotomique.
        
            Examples: 
                racine_carree(16) = 4
                racine_carree(10) = 3
            
            Parameters:
                n (int): Un nombre
            
            Returns:
                Le plancher de la racine carree d'un nombre
        """
        if n == 0:
            return 0

        gauche = 1
        droite = n
        while gauche <= droite:
            milieu = (gauche + droite) // 2
            if milieu <= n // milieu:
                gauche = milieu + 1
            else:
                droite = milieu - 1
        return gauche - 1
    

    def decimal_a_binaire(n: int) -> str:
        """
        6★ Transforme un entier en sa représentation binaire (base 2).
        Plus d'étoiles si vous séparez les bits en blocs de 4.
        
            Examples : 
                28 --> 0001 1100
            
            Parameters:
                n (int): Un nombre en base 10
            
            Returns:
                Le nombre en base 2
        """
        return ""
    

    def  decimal_a_octal(n: int) -> str:
        """
        6★ Transforme un entier en sa représentation octale (base 8).
        Plus d'étoiles si vous séparez les chiffres en blocs de 3.

            Example:
                28 423 --> 067 407

            Parameters:
                n (int): Un nombre en base 10

            Returns:
                Le nombre en base 8
        """
        return ""
    

    def decimal_a_hexa(n: int) -> str:
        """
        6★ Transforme un entier en sa représentation hexadécimale (base 16).
        Plus d'étoiles si vous séparez les bits en blocs de 2.
        Les chiffres en hexadécimal sont : 
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A (10), B (11), C (12), D (13), E (14), F (15)
        
            Example:
                28 423 --> 6F 07
        
            Parameters:
                n (int): Un nombre en base 10

            Returns:
                Le nombre en base 16
        """
        return ""
    

    def nb_de_bits(n: int) -> str:
        """
        ★★★ Calcule le nombre de bits qu'il faut pour écrire un entier
        
            Example:
                3 --> 2
                Il faut 2 bits pour écrire le chiffre 3, car 3 est 11 en binaire.
            
            Parameters:
                n (int): Un entier
            
            Returns:
                Le nombre de bits nécessaires pour l'écrire.
        """
        return -1
    

    def nb_octets(n: int) -> int:
        """
        ★★★ Calcule le nombre d'octets nécessaires pour écrire le nombre. Un octet (byte) vaut 8 bits.
        
            Example:
                255 entre dans 1 octet
                260 entre dans 2 octets
        
            Parameters:
                n (int): Un entier
            
            Returns:
                Le nombre d'octet suffisants pour le contenir
        """
        return -1
    

    def est_premier(n: int) -> bool:
        """
        5★ Détermine si un nombre est premier ou non. Un nombre est premier si 
        ses seuls facteurs sont 1 et lui-même
        
            Example:
                13 est premier
                14 n'est pas premier (14 = 7 * 2)
            
            Parameters :
                n (int): un entier

            Returns:
                True si n est un premier, false sinon.   
        """
        return False
    

    def est_semi_premier(n: int) -> bool :
        """
        5★ Détermine si un nombre est semi-premier. Un nombre est semi-premier s'il a 
        exactement 2 facteurs premiers.
        
            Example:
                299 est semi-premier (299 = 13  * 23)
                300 n'est pas semi-premier (il a trop de facteurs)
        
            Parameters:
                n (int): Un nombre entier
            
            Returns:
                Vrai si le nombre est semi-premier. Faux sinon.
        """
        return False
    

    def facteurs_semi_premier(n: int) -> tuple[bool, int, int]:
        """
        ★★★ Détermine si un nombre est semi-premier. Un nombre est semi-premier s'il a 
        exactement 2 facteurs premiers.
        Si le nombre est semi-premier, la fonction donne en plus ses deux facteurs premiers
        
            Example:
                299 est semi-premier (299 = 13  * 23)
                300 n'est pas semi-premier (il a trop de facteurs)
        
            Parameters:
                n(int): Un nombre entier
            
            Returns: Vrai si le nombre est semi-premier, ainsi que ses facteurs. Faux sinon
        """
        return False, -1, -1
    

    def est_jumeau(n: int) -> bool:
        """
        ★★ Détermine si un nombre est un jumeau. Un nombre n est jumeau s'il est premier
        et que n - 2 ou n + 2 sont premiers.
        
            Example:
                29 et 31 sont jumeaux

            Parameters:
                n(int): Un nombre entier
            Returns:
                Vrai si n est un jumeau, faux sinon
        """
        return False
    

    def est_premier_sophie_germain(n: int) -> bool:
        """
        ★★ Détermine si un nombre est un premier de Sophie Germain.
        Un nombre n est un premier de Sophie Germain si :
            Il est premier et
            2 * n + 1 est premier
        
            Parameters:
                n(int): Un nombre entier

            Returns:
                Vrai si le nombre est un premier de Sophie Germain, faux sinon
        """
        return False
    

    def est_premier_sur(n: int) -> bool:
        """
        ★★ Détermine si un nombre est un premier sûr
        Un nombre n est un premier sûr si :
            Il est premier et
            (n - 1) / 2 est premier
        
            Parameters:
                n(int): Un nombre entier
            Returns:
                Vrai si le nombre est un premier sûr, faux sinon
        """
        return False
    

    def nb_de_chiffres(n: int, c: int) -> int:
        """
        ★★ Trouve la quantité de fois où le chiffre c apparaît dans un nombre en base 10.
        
            Example:
                Il y a 3 zéros dans 10010
    
            Parameters:
                n(int): Un nombre entier
            
            Returns:
                Le nombre de c dans la représentation en base 10 du chiffre
        """
        return -1
    

    def mode(n: int) -> int:
        """
        4★ Trouve le chiffre le plus populaire dans un nombre en base 10.
        
            Example:
                Le mode dans 788_848_388 est 8 (il apparait 6 fois)
                Dans 445566, 4, 5 ou 6 sont des bonnes réponses
    
            Parameters:
                n(int): Un nombre entier

            Returns:
                Le mode de n
        """
        return -1
    

    def somme_des_chiffres(n: int) -> int: 
        """
        ★★ Calcule la somme des chiffres dans un nombre
        
            Example:
                128 --> 1 + 2 + 8 = 11
        
            Parameters:
                n(int): Un nombre entier
        
            Returns:
                La somme des chiffres dans l'entier
        """
        return -1
    

    def somme_des_chiffres_jusqua_un_chiffre(n: int) -> int:
        """
        ★★ Calcule la somme des chiffres dans un nombre et recommence jusqu'à l'obtention
        d'un seul chiffre.
        
        Example:
            128 --> 1 + 2 + 8 = 11 --> 1 + 1 = 2
        
            Parameters:
                n(int): Un nombre entier
            
            Returns:
                La somme des chiffres dans l'entier, récursivement jusquà l'obtention d'un seul chiffre.
        """
        return -1
    

    def est_tout_pareil(n: int) -> bool:
        """
        ★★ Détermine si un nombre est constitué de tout le même chiffre.
        
            Example:
                11111 est tout pareil

            Parameters:
                n(int): Un nombre entier

            Returns:
                Vrai si le nombre est constitué de répétitions du même chiffre, faux sinon.
        """
        return -1
    

    def est_palindrome(n: int) -> str:
        """
        4★ Détermine si un nombre est un palindrome. Un nombre est un palindrome s'il s'écrit
        de la même manière à partir de la gauche et à partir de la droite. Par exemple, 
        les nombres 120021 et 64146 sont des palindromes.
        
            Parameters:
                n(int): Un nombre entier

            Returns:
                Vrai si le nombre est un palindrome, faux sinon.
        """
        return False
    

    def est_dans_fibonacci(n: int) -> bool:
        """
        ★★★ Détermine si un nombre apparait dans la suite de Fibonacci.
        La suite de fibonacci est la suivante :
        0, 1, 1, 2, 3, 5, 8, 13, ...

        Chaque élément est la somme des deux précédents
        
            Parameters :
                n (int): Un nombre entier

            Returns:
                Vrai si le nombre est dans la suite de Fibonacci, faux sinon
        """
        return False
    

    def position_fibonacci(n: int) -> int:
        """
        ★★★ Détermine la position d'un nombre qui apparait dans la suite de Fibonacci. Si le nombre 
        entré n'est pas dans la suite de Fibonacci, la fonction retourne -1.
        
        La suite de fibonacci est la suivante :
        0, 1, 1, 2, 3, 5, 8, 13, ...
        Le 2 est à la position 3.

        Chaque élément est la somme des deux précédents

            Parameters:
                n (int): Un nombre entier
            
            Returns:
                La position de n dans la suite de Fibonacci, s'il en fait partie. -1 sinon
        """
        return -1