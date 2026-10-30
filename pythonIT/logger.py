import json
import os
import platform
import psutil

def bytes_to_gb(value: int) -> float:
    return round(value / (1024 ** 3), 2)

def main():
    data = search_data()
    save_data(data)

def search_data():
    comp_name = f"{platform.node()}_{os.getpid()}"
    memory = psutil.virtual_memory()
    total_memory = bytes_to_gb(memory.total)
    free_memory = bytes_to_gb(memory.available)
    processes = list(psutil.process_iter())
    active_processes = len(processes)
    total_threads = sum(p.num_threads() for p in processes)
    disk = psutil.disk_usage('/')
    used_disk = bytes_to_gb(disk.used)

    data = {
        "имя компьютера": comp_name,
        "общая память (ГБ)": total_memory,
        "свободная память (ГБ)": free_memory,
        "число активных процессов": active_processes,
        "число потоков": total_threads,
        "занятая память на жестком диске (ГБ)": used_disk
    }
    return data

def save_data(data: dict):
    name = "data.json"
    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()