pip install -r requirements.txt --only-binary=:all: --upgrade --platform manylinux2014_x86_64 --implementation cp --python-version 3.10 --target ./dep

pip install -r exceptiongroup --only-binary=:all: --upgrade --platform manylinux2014_x86_64 --implementation cp --python-version 3.10 --target ./dep

move fastapi folder
cd dep

(zip ../lambda_artifact.zip -r .)