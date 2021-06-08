# YOLOV5 baseline

## setting

```shell
git clone https://github.com/ultralytics/yolov5.git

pip install -r requirements.txt
```

## train

```shell
python train.py --img 640 --batch 8 --epochs 100 --data data/0105-crack-div.yaml --device 0 --project 0607_baseline --weights weights/yolov5s.pt --name A
```

## test

```shell
python test.py --batch 8 --data data/0105-crack-div.yaml --device 0 --project 0607_baseline --weights weights/p_s.pt --save-json
```

## 0105-crack-div.yaml

This yaml file is used to specify the path of training set and test set.

```yaml
train: /home/featurize/data/2021-01-03-crack-yolo-B/train/images/
val: /home/featurize/data/2021-01-03-crack-yolo-B/test/images/

nc: 13
names: ['RW','GD','DK','LW','BM','DM','KJ','LSA','LSB','DK2','GD2','CS','HF']
```

