xml = """
<versao>
    1.0
</versao>
"""

with open("config.xml", "w") as f:
    f.write(xml)

with open("config.xml", "r") as f:
    print(f.read())