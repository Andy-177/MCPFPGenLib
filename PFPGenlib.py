from PIL import Image
import os
##################################################################
##################################################################
###                                                            ###
###      #   #        #####      ######     ######    ######   ###
###     # # # #      #     ##    #     #    #         #     #  ###
###    #   #   #     #           ######     ######    ######   ###
###   #         #    #     ##    #          #         #        ###
###  #           #    #####      #          #         #        ###
###                                                            ###
##################################################################
##################################################################
class Segment_skin():
 def __init__(self, skin_path):
     self.skin_path = skin_path
 def cut_skin(self):
     skin = Image.open(self.skin_path).convert('RGBA')
     side_face = skin.crop((5, 9, 8, 16))
     side_face.save('cache/side_face.png')
     face = skin.crop((8, 9, 15, 16))
     face.save('cache/face.png')
     out_side_face = skin.crop((33, 9, 36, 16))
     out_side_face.save('cache/out_side_face.png')
     out_face = skin.crop((40, 9, 47, 16))
     out_face.save('cache/out_face.png')
     body = skin.crop((20, 20, 28, 29))
     body.save('cache/body.png')
     out_body = skin.crop((20, 36, 28,45))
     out_body.save('cache/out_body.png')
     rhand = skin.crop((45, 20, 47, 27))
     rhand.save('cache/rhand.png')
     out_rhand = skin.crop((45, 36, 47, 43))
     out_rhand.save('cache/out_rhand.png')
     lhand = skin.crop((37, 52, 39, 59))
     lhand.save('cache/lhand.png')
     out_lhand = skin.crop((53, 52, 55, 59))
     out_lhand.save('cache/out_lhand.png')
     self.edit_body()
 def edit_body(self):
     edit = Image.open('cache/body.png').convert('RGBA')
     edit.putpixel((0, 0), (0, 0, 0, 0))
     edit.putpixel((7, 0), (0, 0, 0, 0))
     edit.save('cache/body.png')
     edit = Image.open('cache/out_body.png').convert('RGBA')
     edit.putpixel((0, 0), (0, 0, 0, 0))
     edit.putpixel((7, 0), (0, 0, 0, 0))
     edit.save('cache/out_body.png')
##################################################################
##################################################################
class PFPGen():
    def __init__(self):
       pass
    def create_tbg(self):
     bg = Image.new(mode='RGBA', size=(20, 20), color=(0, 0, 0, 0))
     bg.save('cache/background.png')
    def create_bg(self,RGB:tuple):
     bg = Image.new(mode='RGBA', size=(20, 20), color=RGB)
     bg.save('cache/background.png')
    def gen_pfp(self):
        result = Image.open('cache/background.png').convert('RGBA')

        side_face = Image.open('cache/side_face.png').convert('RGBA')
        out_side_face = Image.open('cache/out_side_face.png').convert('RGBA')
        result.paste(side_face,(5,4))
        result.paste(out_side_face,(5,4),out_side_face)

        face = Image.open('cache/face.png').convert('RGBA')
        out_face = Image.open('cache/out_face.png').convert('RGBA')
        result.paste(face,(8,4))
        result.paste(out_face,(8,4),out_face)

        lhand = Image.open('cache/lhand.png').convert('RGBA')
        out_lhand = Image.open('cache/out_lhand.png').convert('RGBA')
        result.paste(lhand,(13,13))
        result.paste(out_lhand,(13,13),out_lhand)

        body = Image.open('cache/body.png').convert('RGBA')
        out_body = Image.open('cache/out_body.png').convert('RGBA')
        result.paste(body,(6,11),body)
        result.paste(out_body,(6,11),out_body)

        rhand = Image.open('cache/rhand.png').convert('RGBA')
        out_rhand = Image.open('cache/out_rhand.png').convert('RGBA')
        result.paste(rhand,(5,13))
        result.paste(out_rhand,(5,13),out_rhand)

        result.save('output/Template.png')
class Sz():
 def __init__(self):
    pass
 def skin_shadow(self):
   Temp = Image.open('output/Template.png').convert('RGBA')
   skinshadow = Image.open('asset/skin_shadow.png').convert('RGBA')
   Temp.paste(skinshadow,(0,0),skinshadow)
   Temp.save('output/Template.png')
 def zoom(self):
   Temp = Image.open('output/Template.png').convert('RGBA')
   resized = Temp.resize((300,300),Image.NEAREST)
   resized.save('output/pfp.png')
 def shader(self):
   pfp = Image.open('output/pfp.png').convert('RGBA')
   shadow = Image.open('asset/shadow.png').convert('RGBA')
   pfp.paste(shadow,(0,0),shadow)
   pfp.save('output/pfp_shadow.png')
class Skin_check():
  def __init__(self,checkpath):
    self.checkpath = checkpath
  def sc(self):
    checkpath = self.checkpath
    check = Image.open(f'{checkpath}')
    width, height = check.size
    if width ==64 and height == 64:
     return(True)
    else:
     print('图片不合规')
     return(False)
class Folder_check():
 def __init__(self):
  self.folder_names = ['cache','output']
 def fc(self):
  for folder_name in self.folder_names:
    if not os.path.exists(folder_name):
       os.makedirs(folder_name)
       print('当前目录下文件夹有缺失，已自动创建')