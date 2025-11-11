from Loader import Loader
from tool import tool
import asyncio
import psutil
import os
from time import sleep
import asyncio

async def run(load: "Loader"):
    for i in load.LoadeadScritps:
        asyncio.create_task(load.runApp(i.getPath()))
        
def main() -> None :
    tool.clear_screen()
    asyncio.run(tool.add_path_modules())
    p = psutil.Process(os.getpid())
    p.nice(psutil.HIGH_PRIORITY_CLASS)
    print("[INFO] Prioridade ajustada para HIGH")
    

if __name__ == "__main__":
    main()
    load = Loader()
    load.init()
    asyncio.run(run(load))