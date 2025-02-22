import json, csv, logging, os, sys 


logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")


def validate_json(data):
 """Проверяет, является ли JSON списком словарей с одинаковыми ключами."""
 if not isinstance(data, list):
		logging.error("Ошибка: JSON должен быть списком объектов.")
		return False
 if not all(isinstance(item,dict)for item in data):
	logging.error("Ошибка: Все элементы в JSON должны быть объектами (dict).")
	return False


 keys=data[0].keys()
 for item in data:
	if item.keys()!=keys:
		logging.error("Ошибка: Не все элементы JSON имеют одинаковые ключи.") 
		return False 
 return True 


def read_json_file(json_filename):
 """Читает JSON из файла."""  
 if not os.path.exists(json_filename): logging.error(f"Файл {json_filename} не найден.")
 return None

 try:
     with open(json_filename, encoding="utf-8") as json_file:
         data = json.load(json_file)
     return data
 except json.JSONDecodeError:
     logging.error("Ошибка: Некорректный JSON.")
     return None



def write_csv_file(data,csv_filename):
 """Записывает данные в CSV.""" 
 try:
 	with open(csv_filename, 'w', newline='',encoding="utf-8") as file:
		writer = csv.writer(file)
		writer.writerow( data[0].keys())

		for row in data:  writer.writerow(row.values())

		logging.info(f"Файл {csv_filename} успешно создан.")  
 except Exception as e:
		logging.error(f"Ошибка при записи CSV: {e}")  


def process_conversion(json_filename, csv_filename):
 """Обрабатывает конвертацию JSON -> CSV.""" 
 data = read_json_file(json_filename)
 if data is None: return
 if not validate_json(data):return
 write_csv_file(data, csv_filename)



if __name__=="__main__":
	if len(sys.argv) < 3:
		logging.error("Ошибка: Укажите входной JSON-файл и выходной CSV-файл.")  
		sys.exit(1)
	
	json_file = sys.argv[1]
	csv_file = sys.argv[2]
	
	process_conversion(json_file, csv_file)
