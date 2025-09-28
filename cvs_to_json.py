import csv, json, os

BASE = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE, "movies_initial.csv")  # tu CSV
json_path = os.path.join(BASE, "movies.json")        # saldrá aquí

records = []
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        title = r.get("title") or r.get("name") or "Sin título"
        description = r.get("description") or r.get("overview") or "Sin descripción"
        genre = r.get("genre") or r.get("genres") or "Desconocido"
        year_raw = r.get("year") or r.get("release_year") or ""
        try:
            year = int(str(year_raw)[:4]) if year_raw else None
        except:
            year = None

        records.append({
            "title": title,
            "description": description,
            "genre": genre,
            "year": year
        })

with open(json_path, "w", encoding="utf-8") as jf:
    json.dump(records, jf, ensure_ascii=False, indent=2)

print(f"Generado {json_path} con {len(records)} registros.")
