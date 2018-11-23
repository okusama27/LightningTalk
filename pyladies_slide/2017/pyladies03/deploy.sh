make html
cp -r build/html/* ../../../../kame_slides/docs/pyladies03/
cd ../../kame_slides/
git pull
git add .
git commit -m 'Uplode slide'
git push
