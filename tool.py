
import os
import platform
from dataclasses import dataclass
import sys
from pathlib import Path
from Data import Data
import json
import subprocess

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    async def add_path_modules():
        if Data.modules_local == None:return
        try:
            for i in Data.modules_local:
                sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), i)))
            return
        except Exception as E:
            print(f"Erro Al Adicionar Os Caminhos Brutos, Erro: {E}")
            return

    def loadJson(DataJsonPath: Path):
        try:
            with DataJsonPath.open("r", encoding="utf-8") as f:
                return json.load(f)
        except IOError as e:
            print(f"[ERRO] Erro ao carregar arquivo json. Erro: {e}")
            return None


    #Project created successfully!