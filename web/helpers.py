import os

all = {
	"python": ["python", "py"],
	"c++": ["g++", "cpp"]
}


def run_code(lang="python", code="", params=""):
	file = f"save.{all[lang][1]}"
	with open(file, "w") as f:f.write(code)
	os.system(f"{all[lang][0]} {file} {params} > tmp")
	os.remove(file)

	with open("tmp", "r") as out:
		p = open("temp", "r")
		prev = p.read()
		p.close()

		n = open("temp", "w")
		n.write(f"{prev}> {out.read()}")
		n.close()

		f = open("temp", "r")
		data = f.read()
		f.close()
	os.remove("tmp")
	return data