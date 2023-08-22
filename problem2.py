import json
json_obj_list = []
with open("image1.txt", "r") as f:
    for line in f:
        split_line = line.split()
        json_obj = {
            "image_rotation": split_line[0],
            "value": {
                "x": float(split_line[1]) * 100,
                "y": float(split_line[2]) * 100,
                "width": float(split_line[3]) * 100,
                "height": float(split_line[4]) * 100,
                "rotation": split_line[0],
                "rectanglelabels": ["object"]
            }
        }
        json_obj_list.append(json_obj)
with open("image1.json", "w") as write_file:
    json.dump(json_obj_list, write_file, indent=4)

