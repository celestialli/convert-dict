import json
import os

import xmltodict

XML_DICT_URL = "https://folkets-lexikon.csc.kth.se/folkets/folkets_sv_en_public.xml"
XDXF_DICT_URL = "https://folkets-lexikon.csc.kth.se/folkets/folkets_sv_en_public.xdxf"


def download_file(url):
    """Download file to application data directory"""
    filename = os.path.basename(url)
    file_path = os.path.join("./", filename)
    if os.path.exists(file_path):
        print(f"File exist, will skip: {file_path}")
        return file_path

    import requests  # Only import inside function to avoid unnecessary dependency

    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("Failed to download file, the url return is not 200.")
    if len(response.content) == 0:
        raise RuntimeError("Failed to download file, the content size is 0.")
    with open(file_path, "wb") as f:
        f.write(response.content)

    print(f"File downloaded: {file_path}")

    return file_path


def quot_filter(s):
    return s.replace("&quot;", '"')


def extract_list_or_str(content):
    if isinstance(content, list):
        return [quot_filter(x["@value"]) for x in content]
    elif isinstance(content, dict):
        return quot_filter(content["@value"])
    else:
        raise RuntimeError("Content is not a list or dict:", content)


def extract_list_or_str_with_key(content, key):
    if isinstance(content, list):
        result = []
        for x in content:
            if key in x and "@value" in x[key]:
                result.append(
                    {"v": quot_filter(x["@value"]), key: quot_filter(x[key]["@value"])}
                )
            else:
                result.append({"v": quot_filter(x["@value"])})
        return result
    elif isinstance(content, dict):
        if key in content and "@value" in content[key]:
            return {
                "v": quot_filter(content["@value"]),
                key: quot_filter(content[key]["@value"]),
            }
        else:
            return {"v": quot_filter(content["@value"])}
    else:
        raise RuntimeError("Content is not a list or dict:", content)


class DictGen:
    def __init__(self, xml_url, xdxf_url):
        self.final_dict = {}
        xml_path = download_file(xml_url)
        xdxf_path = download_file(xdxf_url)

        with open(xml_path, "r", encoding="utf-8") as f:
            xml_str = f.read()
        self.xml_dict = xmltodict.parse(xml_str)

        with open(xdxf_path, "r", encoding="utf-8") as f:
            xdxf_str = f.read()
        self.xdxf_dict = xmltodict.parse(xdxf_str)

    def extract_phonetic_and_audioaddr_in_xdxf(self, word):
        for w in self.xdxf_dict["xdxf"]["lexicon"]["ar"]:
            if w["k"] == word:
                break
        # Phonetic symbol
        try:
            p = w["def"].get("tr", None)
        except KeyError:
            p = None
        # Audio address
        try:
            a = w["def"]["iref"].get("@href", None)
        except KeyError:
            a = None
        return p, a

    def gen(self):
        for w in self.xml_dict["dictionary"]["word"]:
            key = w["@value"]
            try:
                self.final_dict[key] = {"t": extract_list_or_str(w["translation"])}
            except (KeyError, RuntimeError):
                # Problem in translation, we skip these words
                continue

            # Class
            if "@class" in w:
                self.final_dict[key]["c"] = w["@class"]

            if "paradigm" in w:
                # Inflection
                if "inflection" in w["paradigm"]:
                    self.final_dict[key]["i"] = extract_list_or_str(
                        w["paradigm"]["inflection"]
                    )

            # Example
            if "example" in w:
                self.final_dict[key]["e"] = extract_list_or_str_with_key(
                    w["example"], "translation"
                )

            # Idiom
            if "idiom" in w:
                self.final_dict[key]["id"] = extract_list_or_str_with_key(
                    w["idiom"], "translation"
                )

            # Synonym
            if "synonym" in w:
                self.final_dict[key]["s"] = extract_list_or_str_with_key(
                    w["synonym"], "level"
                )

            # Definition
            if "Definition" in w:
                self.final_dict[key]["d"] = extract_list_or_str(w["Definition"])

            p, a = self.extract_phonetic_and_audioaddr_in_xdxf(key)
            # Phonetic symbol
            if p is not None:
                self.final_dict[key]["p"] = p
            # Audio address
            if a is not None:
                self.final_dict[key]["a"] = a

        print(
            f"Generate dict finish, we have {len(self.final_dict)} entries in the dict."
        )

    def save_dict(self, file_path="folkets_sv_en_public.json"):
        with open(file_path, "w") as file:
            json.dump(self.final_dict, file, ensure_ascii=False)


if __name__ == "__main__":
    dictgen = DictGen(XML_DICT_URL, XDXF_DICT_URL)
    dictgen.gen()
    dictgen.save_dict()
