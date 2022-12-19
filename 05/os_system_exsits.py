import os

file_content = """
This is a test
"""

file = 'file1.txt'
if os.path.exists(file):
    prompt = 'This is overwrite the file %s. (Y/N) :' % file
    resp = input(prompt)
    if resp.lower().startswith('y'):
        fd = open(file, 'w')
        fd.write(file_content)
        fd.close()
else:
    pass