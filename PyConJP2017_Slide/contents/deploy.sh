make html
cp -r ./build/html/* ../../../kame_slides/docs/pyconjp2017/
cd ../../../kame_slides/
git pull
git add .
git commit -m 'Uplode slide'
git push
