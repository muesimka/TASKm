
from storage import load_file, save_file
from config import  NAME_FILE_SAVES
collection = load_file(task_list: [], NAME_FILE_SAVES)

def show_collection(task_collection):
    print("=" * 45)
    if not task_collection:
        print("Список задач пуст!")
    else:
        for number, content in enumerate(task_collection):
            parts = content.strip().split("|", 1)
            task_name = parts[0].strip()
            if len(parts) > 1:
                task_content = parts[1].strip()
            else:
                task_content = ""
            print(f"{number + 1}. {task_name}")
            print(f"   Содержание: {task_content}")
    print("=" * 45)

### Показ меню приложения
def show_menu():
    print("1 - Показать задачи")
    print("2 - Добавить задачу")
    print("3 - Редактировать задачу")
    print("4 - Удаление задачи")
    print("5 - Выход")

```