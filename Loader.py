from dataclasses import dataclass,field
from pathlib import Path
from tool import tool
from modules.Script import Script
import subprocess

@dataclass
class Loader:
    LoadeadScritps: list[Script] = field(default_factory=list)
    dataJsonPath:Path = Path(r"C:\\Users\\gustavoquitto-ieg\\AppData\\Roaming\\ScriptManeger\\data.json")

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
    async def runApp(path_local: Path):
        try:
            path_local = Path(path_local)
            ext = path_local.suffix.lower()

            if ext == ".exe":
                subprocess.Popen(str(path_local), shell=False)

            elif ext == ".ps1":  # PowerShell
                subprocess.Popen([
                    "powershell.exe",
                    "-ExecutionPolicy", "Bypass",
                    "-File", str(path_local)
                ], shell=False)

            elif ext == ".py":  # Python script
                subprocess.Popen([
                    "python",
                    str(path_local)
                ], shell=False)

            elif ext == ".bat":  # Batch
                subprocess.Popen([
                    "start cmd.exe", "/c", str(path_local)
                ], shell=True)

            else:
                print(f"[ERRO] Extensão não reconhecida: {ext}")
                return

            print(f"[INFO] Executando: {path_local}")

        except Exception as e:
            print(f"[ERRO] Falha ao executar '{path_local}'. Erro: {e}")