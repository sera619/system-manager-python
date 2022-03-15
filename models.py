import os, sys, random
from PyQt6.QtWidgets import QWidget, QPushButton


class Styles():
    CONTACTBUTTON = """
    QPushButton{
        color: black;
        }
    QPushButton:hover{
        border: 1px solid 50%;
        border-bottom: 2px solid 50%;
        background:rbg(0,107,140) ;
        color: black;
        }
    QPushButton:pressed {
        border: 1px solid 50%;
        border-top: 2px solid 50%;
        background-color: rgb(0,83,140);
        shadow:
        }


    
    """
    PROGRESS = """
    border-radius: 8;

    
    """