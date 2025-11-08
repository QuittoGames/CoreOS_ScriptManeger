from dataclasses import dataclass,field
from pathlib import Path
from tool import tool
from modules.Script import Script
import subprocess

@dataclass
class Loader:
    LoadeadScritps: list[Script] = field(default_factory=list)
    dataJsonPath:Path = Path(r"C:\\Users\\Quitto\\AppData\\Roaming\\ScriptManeger\\data.json")

    def init(self) -> bool:
        dataJson = tool.loadJson(self.dataJsonPath)
        
        if dataJson is None: return False    

        for i in dataJson["scripts"]:
            ScriptLocal = Script(
                id = i["id"],
                name= i["name"],
                scriptPath= i["path"]
            )
            self.LoadeadScritps.append(ScriptLocal)

        return True

    @staticmethod
    def runApp(PathLocal:Path):
        try:
            subprocess.Popen(str(PathLocal), shell=False)
            print(f"[INFO] Executando: {PathLocal}")
        except Exception as e:
            print(f"[ERRO] Falha ao executar '{PathLocal}'. Erro: {e}")