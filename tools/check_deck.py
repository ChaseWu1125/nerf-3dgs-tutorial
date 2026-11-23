import re, glob, os, sys, json
root = sys.argv[1]
wiki = "\n".join(open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(root, "wiki", "**", "*.md"), recursive=True))
order = json.load(open(os.path.join(root, "slides/project/deck.json"), encoding="utf-8"))["order"]
skip_nums = {"1","2","3","4","5","01","02","03","04","05","06","0","10"}
report = []
for sid in order:
    html = open(os.path.join(root, f"slides/project/slides/{sid}.html"), encoding="utf-8").read()
    body = re.sub(r"<x-embed.*?</x-embed>", "", html, flags=re.S)
    body = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", body)
    text = re.sub(r"style=\"[^\"]*\"", "", text)
    has_src = "Wiki：" in text
    refs = re.findall(r"(?:concepts|sources|comparisons)/[\w-]+\.md|misconceptions\.md|index\.md", text)
    missing_refs = [r for r in refs if not os.path.exists(os.path.join(root, "wiki", r))]
    nums = set(re.findall(r"\d+(?:\.\d+)?", text)) - skip_nums
    nums = {n for n in nums if not re.fullmatch(r"20(1|2)\d", n)}  # years
    unfound = sorted(n for n in nums if n not in wiki)
    report.append((sid, has_src, missing_refs, unfound))
for sid, s, m, u in report:
    flag = "OK " if (s or sid=="cover") and not m and not u else "!! "
    print(f"{flag}{sid:13s} src={s} badrefs={m} nums_not_in_wiki={u}")
