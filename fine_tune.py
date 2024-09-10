from ultralytics import YOLO
from ultralytics.data import augment
from ultralytics.utils.loss import FocalLoss
import argparse

from 飞行检测.model_args.args import parse_args

# 使用示例
args = parse_args()

#通用参数
args.model='/workspace/飞行检测/v8s_new/0826_4cls_1024/weights/best.pt'
args.task = 'detect'
args.project = 'fine_tune'
args.name = '0830_6cls_1024'
args.exist_ok = True
args.val = False

#设备参数
args.device = [0, 1]

#训练参数
args.data = '/workspace/飞行检测/data_config/finetune.yaml'
args.epochs = 20
args.batch = 16
args.imgsz = 1024
args.save = True
args.patience = 0
args.optimizer = 'Adam'
args.pretrained = True
args.label_smoothing = 0
args.freeze = 15

args.resume = False

args.box = 7.5
args.cls = 0.05
args.dfl = 1.5
args.lr0 = 0.0001
args.lrf = 0.1
# args.warmup_epochs = 0
args.coslr = True

#数据增强参数
args.mosaic = 0.5
args.close_mosaic = 10
args.copy_paste = 0.3
args.mixup = 0.5
# args.hsv_h = 0.015
# args.hsv_s = 0.7
# args.hsv_v = 0.4
# args.degrees = 0.0
# args.translate = 0.1
# args.scale = 0.5
# args.shear = 0.0
# args.perspective = 0.0
# args.flipud = 0.0
# args.fliplr = 0.5
# args.bgr = 0.0

# YOLO
model = YOLO(model=args.model, task=args.task)  # Load model
model.train(data=args.data, pretrained=args.pretrained, epochs=args.epochs, batch=args.batch, device=args.device, 
            project=args.project, name=args.name, exist_ok=args.exist_ok, save=args.save, resume=args.resume,
            label_smoothing=args.label_smoothing, patience=args.patience, optimizer=args.optimizer, verbose=args.verbose, 
            imgsz=args.imgsz,mosaic=args.mosaic,close_mosaic=args.close_mosaic,copy_paste=args.copy_paste, mixup=args.mixup, # 增强超参数
            cos_lr=args.cos_lr, lr0=args.lr0, lrf=args.lrf,val=args.val,
            warmup_epochs=args.warmup_epochs,freeze=args.freeze,  # 训练超参数
            box=args.box, cls=args.cls, dfl=args.dfl # Train model
            )  


## RT-DETR
# from ultralytics import RTDETR
# # Load a COCO-pretrained RT-DETR-l model
# model = RTDETR("rtdetr-l.yaml")
# # Train the model on the COCO8 example dataset for 100 epochs
# results = model.train(data='./rdd_4.yaml', pretrained=False, epochs=300, batch=32, device=[0, 1], project='rtdetr_no_pre', name='0730', cos_lr=True, 
#             label_smoothing=0.1, patience=20, exist_ok=True, optimizer='auto', verbose=True, copy_paste=.3, 
#             lr0=0.01, lrf=0.01)
