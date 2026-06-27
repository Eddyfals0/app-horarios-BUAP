import os
import re
import csv
import time
import json
from urllib.parse import quote_plus, unquote
import requests
from bs4 import BeautifulSoup

# Paths
CARRERAS_DIR = os.path.join("Carreras", "Ciencias de la computación")
JS_CACHE_PATH = "calificaciones_ia.js"

# Headers for browser simulation
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def load_cached_ratings():
    """Loads existing ratings from calificaciones_ia.js if the file exists."""
    ratings = {}
    if os.path.exists(JS_CACHE_PATH):
        try:
            with open(JS_CACHE_PATH, "r", encoding="utf-8") as f:
                content = f.read()
            
            for line in content.split("\n"):
                line = line.strip()
                if line.startswith('"') and ":" in line:
                    parts = line.split(":", 1)
                    key = parts[0].strip().strip('"')
                    val_str = parts[1].strip().rstrip(",").rstrip("};")
                    
                    if val_str.startswith("{") and val_str.endswith("}"):
                        score_match = re.search(r'score:\s*([0-9.]+)', val_str)
                        url_match = re.search(r'url:\s*"([^"]+)"', val_str)
                        score = float(score_match.group(1)) if score_match else None
                        url = url_match.group(1) if url_match else None
                        ratings[key] = {"score": score, "url": url}
                    else:
                        try:
                            ratings[key] = {"score": float(val_str), "url": None}
                        except ValueError:
                            pass
            print(f"Loaded {len(ratings)} teachers from local cache.")
        except Exception as e:
            print(f"Error reading cache: {e}")
    return ratings

def save_ratings(ratings):
    """Saves the combined ratings dictionary back to calificaciones_ia.js."""
    try:
        lines = ["window.CALIFICACIONES_IA = {"]
        sorted_keys = sorted(list(ratings.keys()))
        for i, key in enumerate(sorted_keys):
            comma = "," if i < len(sorted_keys) - 1 else ""
            val = ratings[key]
            if isinstance(val, dict):
                score_str = f"score: {val['score']}" if val['score'] is not None else "score: null"
                url_str = f'url: "{val["url"]}"' if val['url'] is not None else "url: null"
                lines.append(f'    "{key}": {{ {score_str}, {url_str} }}{comma}')
            else:
                lines.append(f'    "{key}": {{ score: {val}, url: null }}{comma}')
        lines.append("};")
        
        with open(JS_CACHE_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"Successfully saved {len(ratings)} teacher ratings to {JS_CACHE_PATH}")
    except Exception as e:
        print(f"Error saving ratings: {e}")

def get_unique_teachers():
    """Reads all CSVs and returns a set of cleaned teacher names."""
    teachers = set()
    if not os.path.exists(CARRERAS_DIR):
        print(f"Directory {CARRERAS_DIR} not found.")
        return teachers
        
    for file in os.listdir(CARRERAS_DIR):
        if file.endswith(".csv"):
            file_path = os.path.join(CARRERAS_DIR, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        prof = row.get("Profesor", "").strip()
                        if prof and prof != "NO ASIGNADO":
                            # Clean scheduling prefixes like 0800-0859 or 0800-0959 at the beginning of the name
                            cleaned_prof = re.sub(r'^\d{4}-\d{4}\s*', '', prof)
                            teachers.add(cleaned_prof.strip())
            except Exception as e:
                print(f"Error reading {file}: {e}")
    return sorted(list(teachers))

def search_misprofesores_url(teacher_name):
    """Searches Yahoo Search for the teacher's profile URL on misprofesores.com."""
    query = f"site:misprofesores.com BUAP {teacher_name}"
    url = "https://search.yahoo.com/search"
    params = {"q": query}
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"  [Yahoo Search] Failed search request: HTTP {response.status_code}")
            return None
            
        soup = BeautifulSoup(response.text, "html.parser")
        
        for link in soup.find_all("a"):
            href = link.get("href", "")
            decoded_href = unquote(href)
            if "misprofesores.com/profesores/" in decoded_href:
                if "RU=" in decoded_href:
                    actual_url = decoded_href.split("RU=")[1].split("/RK=")[0]
                    # Ensure it starts with protocol
                    if "http" in actual_url:
                        # Decode if still encoded
                        if "%" in actual_url:
                            actual_url = unquote(actual_url)
                        return actual_url
                else:
                    clean_url = decoded_href.split("?")[0]
                    if "https://www.misprofesores.com" in clean_url:
                        return clean_url
    except Exception as e:
        print(f"  [DDG Search] Error searching for {teacher_name}: {e}")
    return None

def scrape_teacher_rating(profile_url):
    """Scrapes the average rating from the teacher's profile page on misprofesores.com."""
    try:
        response = requests.get(profile_url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"  [Profile Scraping] Failed profile request: HTTP {response.status_code}")
            return None
            
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Look for breakdown-container quality -> grade
        quality_div = soup.find("div", class_="breakdown-container quality")
        if quality_div:
            grade_div = quality_div.find("div", class_="grade")
            if grade_div:
                grade_str = grade_div.text.strip()
                try:
                    score = float(grade_str)
                    return score
                except ValueError:
                    print(f"  [Profile Scraping] Non-numeric score found: '{grade_str}'")
        else:
            # Fallback: check other grade classes
            grades = soup.find_all("div", class_="grade")
            if grades:
                try:
                    score = float(grades[0].text.strip())
                    return score
                except ValueError:
                    pass
    except Exception as e:
        print(f"  [Profile Scraping] Error scraping profile page: {e}")
    return None

def main():
    print("=== FCC BUAP Teacher Rating Scraper (IA Database compiler) ===")
    
    # 1. Load cache
    ratings = load_cached_ratings()
    
    # 2. Get unique teachers from CSV
    teachers = get_unique_teachers()
    print(f"Found {len(teachers)} unique teachers in schedule files.")
    
    new_ratings_found = 0
    
    # 3. Process each teacher
    for i, teacher in enumerate(teachers):
        if teacher in ratings:
            # Already exists in cache, skip it to save requests
            continue
            
        print(f"[{i+1}/{len(teachers)}] Investigating: '{teacher}'...")
        
        # Search URL
        profile_url = search_misprofesores_url(teacher)
        if profile_url:
            print(f"  Found profile URL: {profile_url}")
            # Wait a moment to be polite
            time.sleep(1.0)
            
            # Scrape rating
            rating = scrape_teacher_rating(profile_url)
            if rating is not None:
                ratings[teacher] = {"score": rating, "url": profile_url}
                new_ratings_found += 1
                print(f"  Rating extracted: {rating} / 10.0")
                
                # Auto-save changes periodically
                if new_ratings_found % 5 == 0:
                    save_ratings(ratings)
            else:
                print("  Failed to extract score from profile page.")
        else:
            print("  No profile found on misprofesores.com for this teacher.")
            
        # Wait before next search to prevent IP block
        time.sleep(2.0)
        
    # Final save
    save_ratings(ratings)
    print("Scraper run completed successfully.")

if __name__ == "__main__":
    main()
