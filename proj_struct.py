import os

dirs=[
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    'notebooks',
    'saved_models',
    'src'
]

for dirr in dirs:
    os.makedirs(dirr,exist_ok=True)
    with open(os.path.join(dirr,'.gitkeep'),'w') as fd:
        pass

file=[
    'README.md',
    'dvc.yaml',
    'params.yaml',
    os.path.join('src','__init__.py')
]

for f in file:
    with open(f,'w') as ff:
        pass