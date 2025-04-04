import ollama
import json
from tqdm import tqdm
import time
import CONFIG



def run():


    with open("./data/64gua.json", "r", encoding="utf-8") as f:
        gua_data = json.load(f)
        for gua in tqdm(list(gua_data["hexagrams"].values())):
            for idx in range(CONFIG.N_STORY_PER_GUA):
                prompt = CONFIG.PROMPT_TEMPLATE.format(
                    gua_name = gua["chinese_name"],
                    nature = gua["nature"],
                    element = gua["element"],
                    attribute = gua["attribute"],
                    quote = gua["image"] + ";" + gua["judgment"],
                    description = gua["description"]
                )

                start = time.time()
                result = ollama.generate(
                    model = CONFIG.MODEL,
                    prompt = prompt,
                    stream=False
                )
                end = time.time()
                result_data = {
                    "gua_name":gua["chinese_name"],
                    "story":result["response"],
                    "duration":end-start
                }
                with open("./data/64gua_poem.jsonl", "a", encoding="utf-8") as f:
                    f.write(json.dumps(result_data, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    run()