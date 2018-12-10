import json
from pprint import pprint
import os

#get image list
image_path = '/home/artia/prj/datasets/preprocessed_coco/val_edge_detected_without_bg'
image_list = os.listdir(image_path)

# define annotstions list 
annotations_path = '/home/artia/prj/datasets/preprocessed_coco/val_edge_detected_without_bg'
annotations_list = os.listdir(annotations_path)



new_dict = {} # object key value pain
images_info = [] # array value in index
annotations_info = [] # array value of annotations in index 

#how_many_images = 1000
how_many_images = 700

# put info, licenses, categories into new_dict 
with open('person_keypoints_train2017.json') as data_file:
	data = json.load(data_file)
	new_dict['info'] = data['info']
	new_dict['categories'] = data['categories']
	new_dict['licenses'] = data['licenses']

	for file_name in image_list[:how_many_images]:
		for element in data["images"]:
			if os.path.splitext(element['file_name'])[0] == os.path.splitext(file_name)[0]:
				images_info.append(element)
				break

new_dict['images'] = images_info




# annotations from here
# How to get image id list of our processed images
image_id_list = [ item['id'] for item in images_info]
#print(image_id_list[0]) # 407130
########print(image_id_list) # [407130, 35504, 278100, 436544] 
#print(image_id_list)


i = 0


#for image_id in annotations_list[:3]:
for id in annotations_list[:how_many_images]:
	for element in data["annotations"]:
	#for element in data["annotations"][1]["id"]:
		
		a = image_id_list[i]
		#print(data["annotations"][i]["id"]) #183020
		if (a in image_id_list):
		#if os.path.splitext(element['image_id_list[0]'])[0] == os.path.splitext(image_id_list[0])[0]:
		#if os.path.splitext(element['image_id_list'])[0] == os.path.splitext(image_id_list)[0]:
		#if os.path.splitext(element[image_id_list])[0] == os.path.splitext(image_id_list)[0]:
		#if os.path.splitext(element[image_id_list[0]])[0] == os.path.splitext(image_id_list[0])[0]:
			#annotations_info.append(element)
			element = data["annotations"][i]
			i += 1 
			#print(element)
			annotations_info.append(element)
			break
		

		#break

new_dict['annotations'] = annotations_info
print(i)
#########print(new_dict)
with open('processed_person_keypoints_val2017.json', 'w') as outfile:
    json.dump(new_dict, outfile, indent = 4)

#pprint(data['images'][:1])
#pprint(data['images'][:3])

#print(data['annotations'][:1])

#print(data["annotations"][0]["image_id"])
#print(data["annotations"][0]["id"]) #183020
#print(os.path.splitext(file_name)[0])
#print(os.path.splitext(element['file_name'])[0])

# if image_id_list[0] in image_id_list

#pprint(data['categories'][:3])


#########################

# with open('person_keypoints_train2017.json') as data_file:
# 	data = json.load(data_file)

# 	#print(data["images"][1]["file_name"]) # 000000522418.jpg
	# print(data["images"][1]["id"])
#print(data["annotations"][1]["id"])
#print(data["annotations"][2]["id"])
	# print(data["images"][1]["date_captured"])

#print(data.keys()) # dict_keys(['info', 'licenses', 'images', 'annotations', 'categories']) print

#######################################

	# print(data["images"][1]["file_name"]) # 000000522418.jpg
	# print(data["images"][1]["id"])
	# print(data["images"][2]["id"])
	# print(data["images"][3]["id"])
	# print(data["images"][1]["date_captured"])

#########################################################################################################################

# with open('person_keypoints_train2017.json') as data_file:
# 	data = json.load(data_file)
# 	print(data["annotations"][:2])