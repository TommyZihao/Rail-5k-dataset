import json
import os
import os.path as osp
import cv2

from tqdm import tqdm


def split(raw, thres=0.9):
    ids = {obj['image_id'] for obj in raw}
    
    splited = {}
    
    for obj in raw:
        image_id = obj["image_id"]
        if obj["score"] <= thres:
            continue

        if image_id not in splited:
            splited[image_id] = []
            
        splited[image_id].append(obj)
        
    return splited


def dump_one_img(pred_one_img, out_dir):
    image_id = pred_one_img[0]["image_id"]
    with open(osp.join(out_dir, "{}.txt".format(image_id)), mode="w") as f:
        h_img, w_img, _ = cv2.imread("/home/featurize/data/RawImages/{}.jpg".format(image_id)).shape
        for obj in tqdm(pred_one_img):
            x, y, w, h = obj["bbox"]

            x += w / 2
            y += h / 2
            
            x /= w_img
            y /= h_img
            w /= w_img
            h /= h_img
            
            print(obj["category_id"], x, y, w, h, file=f)


thres = 0.9

raw = json.load(open("/home/featurize/yolo-test-0107/p_s_predictions.json"))
splited = split(raw, thres=thres)

os.mkdir("label@{}".format(thres))
for pred_per_img in tqdm(splited.values()):
    dump_one_img(pred_per_img, "label@{}".format(thres))
