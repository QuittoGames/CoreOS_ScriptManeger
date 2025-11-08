from dataclasses import dataclass
from pathlib import Path

@dataclass
class Script:
    name: str
    id: int = 0
    scriptPath: Path | None = None

    def getID(self): return self.id
    def getName(self): return self.name
    def getPath(self): return self.scriptPath

    def setName(self, name: str): self.name = name
    def setPath(self, scriptPath: Path): self.scriptPath = scriptPath
