
import os
from CalculatriceCrypto import CalculatriceCrypto as crypto

# Plus grand double : 9223372036854775807
# Plus grand premier : 9223372036854775783
class Main():
    LARGEUR = 80
    
    def cls():
        """
        Efface le contenu de la console
        """ 
        os.system('cls' if os.name=='nt' else 'clear')

    def convert_int(s:str, default:int) -> int:
        """
        Convertit un string en int, retourne la valeur par défaut si la chaîne ne contient pas un int

            Parameters:
                s(str): Une chaîne de caractères
                default(int): La valeur à retourner si s ne contient pas un nombre

            Returns:
                la valeur int contenue dans s
        """
        try:
            i = int(s)
        except ValueError:
            i = default
        return i


    def mot_important(s:str):
        """
        Affiche à la console la chaîne reçue, en couleur.

            Parameters:
                s(str): Une chaîne de caractères
        """
        print('\033[36m' + s + '\033[0m', end='')

    def imprimer_cadre(left:bool = False, titre:str = None, *lignes: str):
        """
        Imprime des lignes dans un câdre aligné à gauche ou à droite, avec un titre centré.

            Parameters:
                left(bool): Vrai pour alignement à gauche, faux pour alignement droite
                titre(str): Le titre, optionnel
                *lignes(str): les lignes du corps
        """
        Main.mot_important('╔' + (Main.LARGEUR - 2) * '═' + '╗')
        print()
        if titre is not None:
            Main.mot_important('║' + titre.center(Main.LARGEUR - 2) + '║')
            print()
            Main.mot_important('╠' if len(lignes) > 0 else '╚')
            Main.mot_important((Main.LARGEUR - 2) * '═')
            Main.mot_important("╣" if len(lignes) > 0 else "╝")
            print()
        for l in lignes:
            if len(l) > 0:
                Main.mot_important('║')
                if left: 
                    print(l.ljust(Main.LARGEUR - 2), end = '')
                else:
                    print(l.rjust(Main.LARGEUR - 2), end = '')
                Main.mot_important('║')
                print()
        if len(lignes) > 0:
            Main.mot_important('╚' + (Main.LARGEUR - 2) * '═' + '╝')
            print()
        print()
        
    def imprimer_fun_facts(n: int):
        """
        Imprime des faits intéressants à propos du nombre

            Parameters:
                n(int): Un entier positif
        """
        est_palindrome = crypto.est_palindrome(n)
        est_fibonacci = crypto.est_dans_fibonacci(n)
        est_tout_pareil = crypto.est_tout_pareil(n)

        description = 'Il est constitué de : '
        for i in range(10):
            nb_c = crypto.nb_de_chiffres(n, i)
            description += (str(nb_c) + ' ' + str(i) + 's, ') if nb_c > 0 else ''

        Main.imprimer_cadre(
            True,
            f'Faits intéressants à propos de {str(n)}', 
            f'Il faut {str(crypto.nb_octets(n))} octet(s) pour l\'écrire ({str(crypto.nb_de_bits(n))} bits)',
            f'Il est tout pareil' if est_tout_pareil else '',
            description,
            f'Son mode est {str(crypto.mode(n))}',
            f'Sa somme des chiffre est {str(crypto.somme_des_chiffres(n))} ({str(crypto.somme_des_chiffres_jusqua_un_chiffre(n))})',
            f'C\'est un palindrome' if est_palindrome else '',
            f'C\'est le {str(crypto.position_fibonacci(n))}^e nombre de fibonacci' if est_fibonacci else '')

        est_semi_premier,p,q = crypto.facteurs_semi_premier(n)

        est_premier = not est_semi_premier and crypto.est_premier(n)
        if (est_premier or est_semi_premier):
            Main.imprimer_cadre(
                True,
                f'{str(n)} et les nombres premiers',
                f'Il est semi premier. {str(p)}*{str(q)}' if est_semi_premier else ''
                f'Il est premier' + 
                    (' jumeau' if crypto.est_jumeau(n) else '') + 
                    (' de Sophie Germain' if crypto.est_premier_sophie_germain(n) else '') +
                    (' sûr' if crypto.est_premier_sur(n) else '') 
                    if est_premier else '')
    
    def main():
        """
            Imprime des faits intéressants sur un nombre positif choisi par l'utilisateur.
        """
        valide = True
        while valide:
            Main.cls()
            Main.imprimer_cadre(True, '** LA CALCULATRICE DU CRYPTOGRAPHE **')
            n = Main.convert_int(input('Entrez un nombre positif en base 10 '), default = 0)
            valide &= n > 0
            if valide:
                Main.imprimer_cadre(False, None,
                    str(n) +                         ' (décimal) ',
                    str(crypto.decimal_a_binaire(n)) + ' (binaire) ',
                    str(crypto.decimal_a_octal(n))   + ' (octal)   ',
                    str(crypto.decimal_a_hexa(n))    + ' (hex)     ')
                Main.imprimer_fun_facts(n)
                input('Appuyez sur ENTER pour continuer')
        print('Merci d\'avoir utilisé la calculatrice du cryptographe.')
    
if __name__ == '__main__':
    Main.main()