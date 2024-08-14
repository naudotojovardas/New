# Testing site
# from hangman_tdd 

from hangman_tdd import get_word, get_guess, display_hangman, play
import unittest
from unittest.mock import patch


class TestHangman(unittest.TestCase):
    assert get_word()
    assert get_guess()
    assert display_hangman(6) == """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    assert display_hangman(5) == """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """
    assert display_hangman(4) == """
                        --------
                        |      |
                        |      O
                        |      |
                        |
                        |
                        -
                """
    assert display_hangman(3) == """
                        --------
                        |      |
                        |      O
                        |     \|
                        |
                        |
                        -
                """
    assert display_hangman(2) == """
                        --------
                        |      |
                        |      O
                        |     \|/
                        |
                        |
                        -
                """
    assert display_hangman(1) == """
                        --------
                        |      |
                        |      O
                        |     \|/
                        |     /
                        |
                        -
                """
    
    assert display_hangman(0) == """
                        --------    
                        |      |
                        |      O
                        |     \|/
                        |      |
                        |     / \\
                            
                """
    
    assert play('python', 'a') == '______'
    assert play('python', 'p') == 'p_____'
    assert play('python', 'y') == '_y____'
    assert play('python', 't') == '____t_'
    assert play('python', 'h') == '___h__'
    assert play('python', 'o') == '____o_'
    assert play('python', 'n') == '____n'
    assert play('python', 'z') == '______'
    assert play('python', 'python') == 'python'
    assert play('python', 'java') == '______'
    assert play('python', 'javascript') == '______'
    assert play('python', 'python') == 'python'


unittest.main()